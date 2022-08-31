from fastapi import APIRouter
from src.models.models import NodalCalcRequest, NodalCalcResponse
from src.calculations.nodal import calc_nodal

main_router = APIRouter(prefix="/nodal", tags=["NodalAnalysis"])


@main_router.post("/calc", response_model=NodalCalcResponse)
async def post_nodal(data: NodalCalcRequest):
    """
    Эндпоинт для выполнения Узлового Анализа
    """
    # Функция для выполнения узлового анализа
    parsed = data.dict()
    intersect_points = calc_nodal(parsed['vlp'], parsed['ipr'])
    nodal_response = NodalCalcResponse.parse_obj(intersect_points)
    return nodal_response
