import torch
from torch.nn import MSELoss
from geomloss import SamplesLoss


def nll(x_pred, x_true, log_p):
    """ Negative log likelihood """

    return -torch.mean(log_p)


def mse(x_pred, x_true, log_p):
    """ Reconstruction error """

    return MSELoss()(x_pred, x_true)


def make_sinkhorn_divergence(blur=0.05, scaling=0.7, p=2, backend="auto"):
    """
    Creates Sinkhorn divergence loss.

    See http://www.kernel-operations.io/geomloss/api/pytorch-api.html
    """

    sinkhorn = SamplesLoss("sinkhorn", p=p, blur=blur, scaling=scaling, backend=backend)

    def sinkhorn_divergence(x_gen, x_true, log_p):
        return sinkhorn(x_gen, x_true)

    return sinkhorn_divergence
