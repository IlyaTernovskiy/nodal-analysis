from shapely.geometry import LineString, MultiPoint
from src.models.models import NodalCalcDecision

def calc_nodal(vlp: dict, ipr: dict):
    """
    Расчёт точки пересечения VLP vs IPR

    Parameters
    ----------
    vlp : dict
        Словарь, содержащий VLP
    ipr : dict
        Словарь, содержащий IPR
    """
    # Можно использовать numpy или библиотеку Shapely, LineString intersection
    vlp_x = vlp['q_liq']
    vlp_y = vlp['p_wf']
    ipr_x = ipr['q_liq']
    ipr_y = ipr['p_wf']
    vlp_points = list(zip(vlp_x, vlp_y))
    ipr_points = list(zip(ipr_x, ipr_y))
    vlp_curve = LineString(vlp_points)
    ipr_curve = LineString(ipr_points)
    intersect = vlp_curve.intersection(ipr_curve)
    intersect_points = []
    if isinstance(intersect, MultiPoint):
        x = [p.x for p in intersect]
        y = [p.y for p in intersect]
        for i in range(len(x)):
            intersect_point = NodalCalcDecision(**{
                "q_liq": x[i],
                "p_wf": y[i]
            })
            intersect_points.append(intersect_point)
    else:
        intersect_points.append(NodalCalcDecision(**{
            "q_liq": intersect.x,
            "p_wf": intersect.y
        }))
    return intersect_points

