from django.db import connection
from contextlib import closing
def get_otm():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT otm.name as OTM_nomi, otm.created_at, vazirlik.name as Vazirlik_nomi,vazirlik_id FROM otm LEFT JOIN vazirlik 
            on otm.vazirlik_id=vazirlik.id""")
        otms = dict_fetchall(cursor)
        return otms

def get_otm_by_vazirlik_id(vazirlik_id):
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT otm.name,vazirlik.name as Vazirlik_nomi,vazirlik_id FROM otm INNER JOIN vazirlik 
            on otm.vazirlik_id=vazirlik.id WHERE vazirlik.id = %s""",[vazirlik_id])
        otm_vazirlik = dict_fetchall(cursor)
        return otm_vazirlik

def get_talaba():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select ism_familiya,yosh,millat.millat_nomi,fuqarolik.fuqarolik, chet_tili.name as chet_Tili,otm.name as OTM_nomi
            from talaba left join otm on talaba.otm_id=otm.id
			left join millat on talaba.millati_id= millat.id 
			left join fuqarolik on talaba.fuqarolik_id= fuqarolik.id 
			left join chet_tili on talaba.chet_tili_id= chet_tili.id """)
        talaba = dict_fetchall(cursor)
        return talaba

def get_talaba_by_otm():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT talaba.ism_familiya,otm.name as OTM_nomi FROM talaba INNER JOIN otm 
        on talaba.otm_id=otm.id""")
        talaba_hisoboti = dict_fetchall(cursor)
        return talaba_hisoboti


def get_talaba_faoliyati():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT talaba.ism_familiya, sertifikati,erishgan_yutuqlar,ilmiy_yutuqlar,chet_tili.name as Chet_tili FROM talaba INNER JOIN chet_tili
        on talaba.chet_tili_id=chet_tili.id """)
        talaba_faoliyatihisoboti = dict_fetchall(cursor)
        return talaba_faoliyatihisoboti


def get_yangi_ariza():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT ism_familiya, fanlar.id as informatika,fanlar.id as ingliz_tili, fanlar.id as ozbekiston_tarixi,talaba.created_at 
        FROM talaba LEFT JOIN fanlar on talaba.informatika_id = fanlar.id and talaba.ozbekiston_tarixi_id = fanlar.id
        AND talaba.ingliz_tili_id = fanlar.id ORDER by talaba.created_at ASC """)
        yangi_arizalar = dict_fetchall(cursor)
        return yangi_arizalar

def get_status_info(status):
    with closing(connection.cursor()) as cursor:
        cursor.execute(f"""select ism_familiya,otm.name as OTM_nomi,talaba.created_at, status.status as status
            from talaba left join otm on talaba.otm_id=otm.id
			left join status on talaba.status_id = status.id where status in ({str(status).strip("[]")})"""
    )
        status = dict_fetchall(cursor)
    return status


def get_adminstrator():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT xodimlar,otm.name as OTM_nomi FROM xodim 
        LEFT JOIN otm on xodim.otm_id=otm.id""")
        adminstrators = dict_fetchall(cursor)
        return adminstrators


def get_adminstrator_by_id(admin_id):
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT xodimlar,otm.name as OTM_nomi FROM xodim LEFT JOIN otm 
        on xodim.otm_id=otm.id WHERE xodim.id=%s""", [admin_id])
        adminstrator = dict_fetchone(cursor)
        return adminstrator




def dict_fetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

def dict_fetchone(cursor):
    row = cursor.fetchone()
    if row is None:
        return False
    columns = [col[0] for col in cursor.description]
    return dict(zip(columns, row))
