from fastapi import APIRouter


router = APIRouter()

@router.get('/test')
def testing():
    print("api-hit")
    return {"status":"ok"}
