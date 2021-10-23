from django.db import models


class Vazirlik(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        db_table = "vazirlik"

    def __str__(self):
        return self.name


class Viloyatlar(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        db_table = "viloyat"

    def __str__(self):
        return self.name


class Tumanlar(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    viloyat = models.ForeignKey(Viloyatlar, blank=False, null=True, on_delete=models.SET_NULL)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        db_table = "tuman"

    def __str__(self):
        return self.name


class Millat(models.Model):
    millat_nomi = models.CharField(max_length=100, blank=False, null=False)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        db_table = "millat"

    def __str__(self):
        return self.millat_nomi


class Fuqarolik(models.Model):
    fuqarolik = models.CharField(max_length=100, blank=False, null=False)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        db_table = "fuqarolik"

    def __str__(self):
        return self.fuqarolik


class OTM_turi(models.Model):
    types = models.CharField(max_length=100, blank=False, null=False)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        db_table = "otm_turi"

    def __str__(self):
        return self.types


class OTM(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    otm_type = models.ForeignKey(OTM_turi, blank=False, null=True, on_delete=models.SET_NULL)
    vazirlik = models.ForeignKey(Vazirlik, blank=False, null=True, on_delete=models.SET_NULL)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        db_table = "otm"

    def __str__(self):
        return self.name


class Talim_turi(models.Model):
    talim_turi_nomi = models.CharField(max_length=50, blank=False, null=False)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        db_table = "talim_turi"

    def __str__(self):
        return self.talim_turi_nomi


class Talim_shakli(models.Model):
    talim_shakli_nomi = models.CharField(max_length=50, blank=False, null=False)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        db_table = "talim_shakli"

    def __str__(self):
        return self.talim_shakli_nomi


class Oquv_yili(models.Model):
    oquv_yili = models.CharField(max_length=50, blank=False, null=False)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        db_table = "oquv_yili"

    def __str__(self):
        return self.oquv_yili


class Oquv_kursi(models.Model):
    kurs = models.CharField(max_length=100, blank=False, null=False)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        db_table = "oquv_kursi"

    def __str__(self):
        return self.kurs


class Talim_yonalishi(models.Model):
    yonalish_nomi = models.CharField(max_length=100, blank=False, null=False)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        db_table = "talim_yonalishi"

    def __str__(self):
        return self.yonalish_nomi


class Fanlar(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        db_table = "fanlar"

    def __str__(self):
        return self.name


class Chet_tili(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        db_table = "chet_tili"

    def __str__(self):
        return self.name


class Chet_tili_sertifikatlari(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        db_table = "sertifikat"

    def __str__(self):
        return self.name


class Chet_tili_darajasi(models.Model):
    darajalar = models.CharField(max_length=100, blank=False, null=False)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        db_table = "daraja"

    def __str__(self):
        return self.darajalar


class Erishgan_yutuqlar(models.Model):
    yutuqlar_nomi = models.CharField(max_length=100, blank=False, null=False)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        db_table = "yutuqlar"

    def __str__(self):
        return self.yutuqlar_nomi


class Ilmiy_yutuqlar_turi(models.Model):
    yutuqlar_turi = models.CharField(max_length=100, blank=False, null=False)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        db_table = "yutuqlar_turi"

    def __str__(self):
        return self.yutuqlar_turi


class Ilmiy_yutuqlar(models.Model):
    yutuqlar_nomi = models.CharField(max_length=100, blank=False, null=False)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        db_table = "ilmiy_yutuqlar"

    def __str__(self):
        return self.yutuqlar_nomi


class Stependiyalar(models.Model):
    nomi = models.CharField(max_length=100, blank=False, null=False)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        db_table = "stependiya"

    def __str__(self):
        return self.nomi


class Tanlov_turi(models.Model):
    tanlov_turi = models.CharField(max_length=100, blank=False, null=False)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        db_table = "tanlov_turi"

    def __str__(self):
        return self.tanlov_turi


class Ariza_holati(models.Model):
    arizalar = models.CharField(max_length=100, blank=False, null=False)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        db_table = "ariza"

    def __str__(self):
        return self.arizalar


class Ariza_statusi(models.Model):
    status = models.CharField(max_length=100, blank=False, null=False)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        db_table = "status"

    def __str__(self):
        return self.status


class Administrator_royxati(models.Model):
    xodimlar = models.CharField(max_length=100, blank=False, null=False)
    otm = models.ForeignKey(OTM, blank=False, null=True, on_delete=models.SET_NULL)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        db_table = "xodim"

    def __str__(self):
        return self.xodimlar


class Talaba(models.Model):
    ism_familiya = models.CharField(max_length=50, blank=False, null=False)
    t_yil = models.IntegerField(blank=False, null=False, default=1)
    yosh=models.IntegerField(blank=False, null=False, default=1)
    pasport_seriya=models.CharField(max_length=30,blank=False,null=False)
    fuqarolik=models.ForeignKey(Fuqarolik,blank=False,null=True,on_delete=models.SET_NULL)
    millati=models.ForeignKey(Millat,blank=False,null=True,on_delete=models.SET_NULL)
    tugilgan_viloyat=models.ForeignKey(Viloyatlar,blank=False,null=True,on_delete=models.SET_NULL)
    t_tuman=models.ForeignKey(Tumanlar,blank=False,null=True,on_delete=models.SET_NULL)
    otm=models.ForeignKey(OTM,blank=False,null=True,on_delete=models.SET_NULL)
    talim_turi=models.ForeignKey(Talim_turi,blank=False,null=True,on_delete=models.SET_NULL)
    talim_shakli=models.ForeignKey(Talim_shakli,blank=False,null=True,on_delete=models.SET_NULL)
    talim_yonalishi=models.ForeignKey(Talim_yonalishi,blank=False,null=True,on_delete=models.SET_NULL)
    oquv_yili=models.ForeignKey(Oquv_yili,blank=False,null=True,on_delete=models.SET_NULL)
    oquv_kursi=models.ForeignKey(Oquv_kursi,blank=False,null=True,on_delete=models.SET_NULL)
    chet_tili=models.ForeignKey(Chet_tili,blank=False,null=True,on_delete=models.SET_NULL)
    sertifikati=models.ForeignKey(Chet_tili_sertifikatlari,blank=False,null=True,on_delete=models.SET_NULL)
    darajasi=models.ForeignKey(Chet_tili_darajasi,blank=False,null=True,on_delete=models.SET_NULL)
    erishgan_yutuqlar=models.ForeignKey(Erishgan_yutuqlar,blank=False,null=True,on_delete=models.SET_NULL)
    ilmiy_yutuqlar=models.ForeignKey(Ilmiy_yutuqlar,blank=False,null=True,on_delete=models.SET_NULL)
    fan_baholari=models.ForeignKey(Fanlar,blank=False,null=True,on_delete=models.SET_NULL)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        db_table = "talaba"

    def __str__(self):
        return self.ism_familiya

class Talaba_xisoboti(models.Model):
    talaba = models.ForeignKey(Talaba, blank=False, null=True, on_delete=models.SET_NULL)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        db_table = "talaba_xisoboti"

    def __str__(self):
        return self.talaba

class Talaba_faoliyati_xisoboti(models.Model):
    talaba = models.ForeignKey(Talaba, blank=False, null=True, on_delete=models.SET_NULL)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        db_table = "talaba_faoliyati"

    def __str__(self):
        return self.talaba

class Yangi_arizalar(models.Model):
    talaba = models.ForeignKey(Talaba, blank=False, null=True, on_delete=models.SET_NULL)
    status = models.ForeignKey(Ariza_statusi, blank=False, null=True, on_delete=models.SET_NULL)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        db_table = "yangi_ariza"

    def __str__(self):
        return self.talaba

class Qabul_qilingan_arizalar(models.Model):
    talaba = models.ForeignKey(Talaba, blank=False, null=True, on_delete=models.SET_NULL)
    status = models.ForeignKey(Ariza_statusi, blank=False, null=True, on_delete=models.SET_NULL)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        db_table = "qabul_ariza"

    def __str__(self):
        return self.talaba

class Rad_qilingan_arizalar(models.Model):
    talaba = models.ForeignKey(Talaba, blank=False, null=True, on_delete=models.SET_NULL)
    status = models.ForeignKey(Ariza_statusi, blank=False, null=True, on_delete=models.SET_NULL)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        db_table = "rad_ariza"

    def __str__(self):
        return self.talaba