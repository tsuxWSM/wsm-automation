from enum import Enum


class SupportedBrowsers(Enum):
    CHROME = "CHR"
    FIREFOX = "FFX"


class Site(Enum):
    SDC = "SDC"
    HHP = "HHP"
    EMP = "EMP"
    KTP = "KTP"
    CVL = "CVL"
    PSU = "PSU"
    RVR = "RVR"
    EIB = "EIB"
