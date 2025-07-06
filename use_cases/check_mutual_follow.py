# app/use_cases/check_mutual_follow.py
from infrastructure.db.mysql_connection import get_userprofile_session
from infrastructure.db.mysql_models import Followers

def check_mutual_follow(id_user_1, id_user_2):
    session = get_userprofile_session()

    follow_1_to_2 = session.query(Followers).filter_by(
        Id_Follower=id_user_1, Id_Following=id_user_2, Status=1
    ).first()

    follow_2_to_1 = session.query(Followers).filter_by(
        Id_Follower=id_user_2, Id_Following=id_user_1, Status=1
    ).first()

    session.close()

    is_mutual = bool(follow_1_to_2 and follow_2_to_1)
    return {"mutual": is_mutual}, 200
