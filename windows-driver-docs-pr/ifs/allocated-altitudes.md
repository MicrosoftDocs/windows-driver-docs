---
title: Allocated Filter Altitudes
description: Lists file system filter altitudes allocated by Microsoft
ms.date: 12/06/2023
keywords:
- filter driver altitude
- minifilter driver altitude
ms.custom: UpdateFrequency1
---

# Allocated filter altitudes

This page lists filter altitude allocations by load order group. It's updated 1-2 times per year, so might not include any recently assigned allocations.

* If you don't have a Microsoft-assigned altitude in the appropriate load order group, [you need to request one](minifilter-altitude-request.md).
* If you already have a Microsoft-assigned "integer" altitude, you can use it to [create your own "fractional" altitude to place a new filter in the same load order group](load-order-groups-and-altitudes-for-minifilter-drivers.md#create-an-altitude).

To learn more about load order groups and altitudes, see [Load order groups and altitudes for minifilter drivers](load-order-groups-and-altitudes-for-minifilter-drivers.md).

To see how a driver uses its altitude number in its INF file, see [Creating an INF file for a filter driver](creating-an-inf-file-for-a-minifilter-driver.md).

## 420000 - 429999: Filter

| Minifilter                  | Altitude | Company                                 |
|-----------------------------|----------|-----------------------------------------|
| ntoskrnl.exe | 425500 | Microsoft |
| ntoskrnl.exe | 425000 | Microsoft |

## 400000 - 409999: FSFilter Top

| Minifilter                  | Altitude | Company                                 |
|-----------------------------|----------|-----------------------------------------|
| wcnfs.sys | 409900 | Microsoft |
| bindflt.sys | 409800 | Microsoft |
| cldflt.sys | 409500 | Microsoft |
| iorate.sys | 409010 | Microsoft |
| ioqos.sys | 409000 | Microsoft |
| fsdepends.sys | 407000 | Microsoft |
| sftredir.sys | 406000 | Microsoft |
| dfs.sys | 405000 | Microsoft |
| WorkplaceContainerDriver.sys | 404960.5 | Venn Technology Corporation |
| IntelEgDriver.sys | 404950.5 | Intel Corp |
| VeeamFCT.sys | 404920 | Veeam Software |
| sek.sys | 404915.5 | Sentry Corporation |
| tracker.sys | 404910 | Acronis |
| csvnsflt.sys | 404900 | Microsoft |
| csvflt.sys | 404800 | Microsoft |
| Microsoft.Uev.AgentDriver.sys | 404710 | Microsoft |
| AppvVfs.sys | 404700 | Microsoft |
| CCFFilter.sys | 404600 | Microsoft |
| cr.sys | 403900.5 | Xryus Technologies Ltd. |
| BGMinFlt.sys | 403100.5 | Virtual Bodyguard BV |
| FwDI.sys | 402130.5 | First Watch Limited |
| 360AntiSteal.sys | 402120.5 | 360 Software (Beijing) |
| uberAgentDrv.sys | 402110 | vast limits GmbH |
| mrigflt.sys | 402100 | Paramount Software Ltd |
| darkscope-drv.sys | 402030.5 | Zhuhai YiZhiSec co |
| XCOAmon.sys | 402025.5 | TRIART INC |
| RevoNetDriver.sys | 402020 | J's Communication Co. |
| dciogrd.sys | 402010 | Datacloak Tech |
| Dewdrv.sys | 402000 | Dell Technologies |
| zsusbstorfilt.sys | 401910 | Zshield Inc |
| eaw.sys | 401900 | Raytheon Cyber Solutions |
| TVFsfilter.sys | 401800 | TrustView |
| KKDiskProtecter.sys | 401700 | Goldmsg |
| AgentComm.sys | 401600 | Trustwave Holding Inc |
| rvsavd.sys | 401500 | CJSC Returnil Software |
| DGMinFlt.sys | 401410 | Digital Guardian Inc. |
| dgdmk.sys | 401400 | Verdasys Inc. |
| stadrv6x64.sys | 401350.5 | Netskope Inc. |
| stadrv6x32.sys | 401350.5 | Netskope Inc. |
| tusbstorfilt.sys | 401300 | SimplyCore LLC |
| pcgenfam.sys | 401200 | Soluto |
| atrsdfw.sys | 401100 | Altiris |
| tpfilter.sys | 401000 | RedPhone Security |
| MBIG2Prot.sys | 400920 | Malwarebytes Inc |
| mbamwatchdog.sys | 400900 | Malwarebytes Corporation |
| DSESafeCtrlDrv.sys | 400803 | Shanghai Eff-Soft IT |
| edevmonm.sys | 400800.3 | ESET spol. s r.o. |
| edevmon.sys | 400800 | ESET spol. s r.o. |
| vmwprotect.sys | 400700.5 | VMware, Inc. |
| vmwcdrfilter.sys | 400700.3 | VMware, Inc. |
| vmwflstor.sys | 400700 | VMware, Inc. |
| TsQBDrv.sys | 400600 | Tencent Technology |
| PolyPortFlt.sys | 400490 | PolyPort Inc |
| Dscdriver.sys | 400300 | Dell Technologies Inc. |

## 360000 - 389999: FSFilter Activity Monitor

| Minifilter                  | Altitude | Company                                 |
|-----------------------------|----------|-----------------------------------------|
| csfsflt.sys | 389550.5 | Darktrace Holdings Ltd. |
| tactical.sys | 389540.5 | Tactical Defense |
| EDRMiniFilter.sys | 389526.5 | Venustech |
| zd_mon.sys | 389520.5 | Zecurion |
| icrlmonitor.sys | 389518.5 | Delta Electronics Inc |
| klboot.sys | 389510 | Kaspersky Lab |
| klfdefsf.sys | 389500 | Kaspersky Lab |
| JKMCPF.sys | 389492.7 | JiranData Co. Ltd |
| JDEDRPF.sys | 389492.5 | JiranData Co. Ltd |
| JDPPWF.sys | 389492 | JiranData Co. Ltd |
| JDPPSF.sys | 389490 | JiranData Co. Ltd |
| FFDriver.sys | 389470 | ColorTokens |
| evaccin.sys | 389455.5 | databps.com |
| SeRdr.sys | 389450 | rhipe Australia Pty |
| bw_fssec.sys | 389430.5 | Wuhan Buwei Software Technology Co., Ltd |
| SecurityPro.sys | 389430.3 | Wuhan Buwei Software Technology Co., Ltd |
| defragger.sys | 389420 | Microsoft |
| storagedrv.sys | 389400 | SMTechnology Co. |
| kixprotect.sys | 389370.5 | SBS Software |
| cydanix_amon.sys | 389350.5 | Cydanix LLC |
| nargflti.sys on 32bit | 389340.6 | NETAND Co.,Ltd |
| nargflta.sys on 64bit | 389340.6 | NETAND Co.,Ltd |
| naspflti.sys on 32bit | 389340.5 | NETAND Co.,Ltd |
| naspflta.sys on 64bit | 389340.5 | NETAND Co.,Ltd |
| NetPeeker.sys | 389330 | eMingSoftware Inc |
| path8flt.sys | 389320 | Telefónica Digital |
| DLPDriverNfn.sys | 389310.5 | Acronis |
| NgScan.sys | 389310 | Acronis |
| icrlmonitor.sys | 389300 | Industrial Technology |
| gibepcore.sys | 389290 | Group-IB LTD |
| cpflt.sys | 389285.5 | Cloudplan GmbH |
| enmon.sys | 389280 | OpenText Corp |
| bfdrv.sys | 389275.5 | KForensic |
| wsafefilter.sys | 389272 | WidgetNuri Corp |
| RansomDetect.sys | 389270 | WidgetNuri Corp |
| PPLPMFilter.sys | 389265.5 | PolicyPak Software |
| cbfsfilter2017.sys | 389260 | Mobile Content Mgmt |
| cbfilter20.sys | 389251 | SecureLink Inc. |
| CBFSFilter2017.sys | 389250 | SecureLink Inc. |
| GmBase.sys | 389248 | NanJing Geomarking |
| MagicProtect.sys | 389247 | NanJing Geomarking |
| cbfsfilter2017.sys | 389245 | NanJing Geomarking |
| cbfsfilter2020.sys | 389245 | NanJing Geomarking |
| DTDSel.sys | 389242 | DELL Technologies |
| NWEDriver.sys | 389240 | Dell Technologies |
| cytmon.sys | 389230 | Cytrence Inc |
| ZtacFltr.sys | 389225.5 | Blackpoint Cyber |
| SophosED.sys | 389220 | Sophos |
| MonsterK.sys | 389210 | Somma Inc |
| MSSITDIF.SYS | 389205.8 | ISNET Corp |
| MSSIDRVF.SYS | 389205.6 | ISNET Corp |
| BMFWTDIF.SYS | 389205.4 | ISNET Corp |
| STORVXFT.SYS | 389205.2 | ISNET Corp |
| STORV1FT.SYS | 389205.1 | ISNET Corp |
| IFS64.sys | 389200 | Ashampoo Development |
| TSTFsReDir.sys | 389192 | ThinScale Tech |
| TSTRegReDir.sys | 389191 | ThinScale Tech |
| TSTFilter.sys | 389190 | ThinScale Tech |
| VrnsFilter.sys | 389180 | Varonis Ltd |
| slb_guard.sys | 389175 | Lenovo Beijing |
| lrtp.sys | 389170 | Lenovo Beijing |
| ipcomfltr.sys | 389160 | Bluzen Inc |
| oneagent.sys | 389155.5 | BluSapphire Cyber Systems Pvt Ltd |
| SvCBT.sys | 389150 | Spharsoft Technologies |
| mbamshuriken.sys | 389140 | Malwarebytes |
| FGFLT.sys | 389135.5 | WinAbility Software |
| ContainerMonitor.sys | 389130 | Aqua Security |
| cmflt.sys | 389125 | Certero |
| SaMFlt.sys | 389120 | DreamCrafts |
| RuiMinispy.sys | 389117 | RuiGuard Ltd |
| RuiFileAccess.sys | 389115 | RuiGuard Ltd |
| RuiEye.sys | 389113 | RuiGuard Ltd |
| RuiMachine.sys | 389111 | RuiGuard Ltd |
| windd.sys | 389110 | Comae Tech |
| cbfsfilter2017.sys | 389105 | Basein Networks |
| taobserveflt.sys | 389100 | ThinAir Labs Inc |
| fsrvlock.sys | 389098 | Man Technology Inc |
| bsrfsflt.sys | 389096 | Man Technology Inc |
| fsrfilter.sys | 389094 | Man Technology Inc |
| vollock.sys | 389092 | Man Technology Inc |
| drbdlock.sys | 389090 | Man Technology Inc |
| dcfsgrd.sys | 389085 | Datacloak Tech |
| hsmltmon.sys | 389080 | Hitachi Solutions |
| AternityRegistryHook.sys | 389070 | Aternity Ltd |
| MozyNextFilter.sys | 389068 | Carbonite Inc |
| MozyCorpFilter.sys | 389067 | Carbonite Inc |
| MozyEntFilter.sys | 389066 | Carbonite Inc |
| MozyOEMFilter.sys | 389065 | Carbonite Inc |
| MozyEnterpriseFilter.sys | 389064 | Carbonite Inc |
| MozyProFilter.sys | 389063 | Carbonite Inc |
| MozyHomeFilter.sys | 389062 | Carbonite Inc |
| BDSFilter.sys | 389061 | Carbonite Inc |
| CSBFilter.sys | 389060 | Carbonite Inc |
| f_pmf.sys | 389055.5 | Fasoo Inc. |
| ChemometecFilter.sys | 389050 | ChemoMetec |
| bcloudsafe.sys | 389045.5 | AISHU Technology Corp |
| SentinelMonitor.sys(retired - new altitude allocated) | 389040 | SentinelOne |
| DhWatchdog.sys | 389030 | Microsoft |
| edrsensor.sys | 389025 | Bitdefender SRL |
| bdprivmon.sys | 389022 | Bitdefender SRL |
| NpEtw.sys | 389020 | Koby Kahane |
| OczMiniFilter.sys | 389010 | OCZ Storage |
| ielcp.sys | 389004 | Intel Corporation |
| IESlp.sys | 389002 | Intel Corporation |
| IntelCAS.sys | 389000 | Intel Corporation |
| neucloak.sys | 388995.5 | NeuShield, Inc. |
| boxifier.sys | 388990 | Kenubi |
| SamsungRapidFSFltr.sys | 388980 | NVELO Inc. |
| drsfile.sys | 388970 | MRY Inc. |
| CbFltFs4.sys | 388966 | Simopro Technology |
| CrUnCopy.sys | 388964 | Shenzhen CloudRiver |
| aictracedrv_am.sys | 388960 | AI Consulting |
| fiopolicyfilter.sys | 388954 | SanDisk Inc. |
| sodatpfl.sys | 388951 | SODATSW spol. s r.o. |
| sodatpfl.sys | 388950.2 | SODATSW |
| fcontrol.sys | 388950 | SODATSW spol. s r.o. |
| qfilter.sys | 388940 | Quorum Labs |
| Redlight.sys | 388930 | Trustware Ltd |
| ClumioChangeBlockMf.sys | 388925 | Clumio Inc |
| eps.sys | 388920 | Lumension |
| VHDTrack.sys | 388915 | Intronis Inc |
| VHDDelta.sys | 388912 | Niriva LLC |
| FSTrace.sys | 388910 | Niriva LLC |
| spidermon.sys | 388905.5 | Guangzhou Shizhen Information Technology Co.,Ltd |
| YahooStorage.sys | 388900 | Yahoo Japan Corporation |
| KeWF.sys | 388890 | KEBA AG |
| epregflt.sys | 388888 | Check Point Software |
| epklib.sys | 388886 | Check Point Software |
| zsfprt.sys | 388880 | k4solution Co., Ltd. |
| dsflt.sys | 388876 | cEncrypt |
| bfaccess.sys | 388872 | bitFence Inc. |
| xcpl.sys | 388870 | X-Cloud Systems |
| DRMFilter.sys | 388867.5 | ManageEngine Zoho |
| DFMFilter.sys | 388867 | ManageEngine Zoho |
| DCFAFilter.sys | 388866 | ManageEngine Zoho |
| RMPHVMonitor.sys | 388865 | ManageEngine Zoho |
| FAPMonitor.sys | 388864 | ManageEngine Zoho |
| FACEDrv.sys | 388863.5 | ManageEngine Zoho |
| MEARWFltDriver.sys | 388863 | ManageEngine Zoho |
| SerMonDriver.sys | 388862.5 | ManageEngine Zoho |
| EaseFlt.sys | 388860 | EaseVault Technologies Inc. |
| rpwatcher.sys | 388855 | Best Security |
| sieflt.sys | 388852 | Quick Heal Technologies Pvt. Ltd. |
| cssdlp.sys | 388851 | Quick Heal Technologies Pvt. Ltd. |
| cssdlp.sys | 388850 | CoSoSys |
| INISBDrv64.sys | 388840 | Initech Inc. |
| kconv.sys | 388832 | Fitsec Ltd |
| trace.sys | 388831 | Fitsec Ltd |
| SandDriver.sys | 388830 | Fitsec Ltd |
| dskmn.sys | 388820 | Honeycomb Technologies |
| offsm.sys | 388811 | Jiransoft Co., Ltd |
| xkfsfd.sys | 388810 | Jiransoft Co., Ltd |
| JKPPOB.sys | 388808 | Jiransoft Co., Ltd |
| JKPPXK.sys | 388807 | Jiransoft Co., Ltd |
| JKPPPF.sys | 388806 | Jiransoft Co., Ltd |
| JKPPOK.sys | 388805 | Jiransoft Co., Ltd |
| pcpifd.sys | 388800 | Jiransoft Co., Ltd |
| NNTInfo.sys | 388790 | New Net Technologies Limited |
| NmpFilter.sys | 388781 | IBM |
| FsMonitor.sys | 388780 | IBM |
| PRFFilter.sys | 388770.5 | CommVault Systems, Inc. |
| CVCBT.sys | 388770 | CommVault Systems, Inc. |
| AwareCore.sys | 388760 | TaaSera Inc. |
| laFS.sys | 388750 | NetworkProfi Ltd |
| fsnk.sys | 388740 | SoftPerfect Research |
| RGNT.sys | 388730 | HFN Inc. |
| fltRs329.sys | 388720 | Secured Globe Inc. |
| ospmon.sys | 388710 | SC ODEKIN SOLUTIONS SRL |
| edsigk.sys | 388700 | Enterprise Data Solutions, Inc. |
| fiometer.sys | 388692 | Fusion-io |
| dcSnapRestore.sys | 388690 | Fusion-io |
| SytSelfProtect.sys | 388688.5 | Sunyata Electronic Tech |
| fam.sys | 388680 | Quick Heal Technologies Pvt. Ltd. |
| vidderfs.sys | 388675 | Vidder Inc. |
| Tritiumfltr.sys | 388670 | Tritium Inc. |
| HexisFSMonitor.sys | 388660 | Hexis Cyber Solutions |
| BlackbirdFSA.sys | 388650 | BeyondTrust Inc. |
| TMUMS.sys | 388642 | Trend Micro Inc. |
| hfileflt.sys | 388640 | Trend Micro Inc. |
| TMUMH.sys | 388630 | Trend Micro Inc. |
| AcDriver.sys | 388620 | Trend Micro, Inc. |
| SakFile.sys | 388610 | Trend Micro, Inc. |
| SakMFile.sys | 388600 | Trend Micro, Inc. |
| rsfdrv.sys | 388580 | Clonix Co |
| alcapture.sys | 388570 | Airlock Digital Pty Ltd |
| kmNWCH.sys | 388560 | IGLOO SECURITY, Inc. |
| ISIRMFmon.sys | 388550 | ALPS SYSTEM INTERGRATION CO., LTD |
| EsProbe.sys | 388542 | Stormshield |
| heimdall.sys | 388540 | Arkoon Network Security |
| thetta.sys | 388532 | Syncopate |
| thetta.sys | 388531 | Syncopate |
| thetta.sys | 388530 | Syncopate |
| DTPL.sys | 388520 | CONNECT SHIFT LTD |
| CyOptics.sys | 388514 | Cylance Inc. |
| CyProtectDrv32.sys | 388510 | Cylance Inc. |
| CyProtectDrv64.sys | 388510 | Cylance Inc. |
| tbfsfilt.sys | 388500 | Third Brigade |
| IvAppMon.sys | 388491 | Ivanti |
| LDSecDrv.sys | 388490 | LANDESK Software |
| SGResFlt.sys | 388480 | Samsung SDS Ltd |
| CwMem2k64.sys | 388470 | ApSoft |
| axfltdrv.sys | 388460 | Axact Pvt Ltd |
| RMDiskMon.sys | 388450 | Qingdao Ruanmei Network Technology Co., Ltd. |
| diskactmon.sys | 388440 | Qingdao Ruanmei Network Technology Co., Ltd. |
| BlackCat.sys | 388435 | NEXON KOREA |
| Codex.sys | 388430 | GameHi Co., Ltd. |
| CatMF.sys | 388420 | Logichron Inc |
| RW7FsFlt.sys | 388410 | PJSC KP VTI |
| aswSP.sys | 388401 | Avast Software |
| aswFsBlk.sys | 388400 | ALWIL Software |
| AbrPmon.sys | 388390 | FastTrack Software ApS |
| ThreatStackFIM.sys | 388380 | Threat Stack |
| BOsCmFlt.sys | 388370 | Barkly Protects Inc. |
| BOsFsFltr.sys | 388370 | Barkly Protects Inc. |
| Asgard.sys | 388365 | SPEKNET EOOD |
| FeKern.sys | 388360 | FireEye Inc. |
| fhfs.sys | 388355.5 | SecureCircle |
| libwaacd.sys | 388350.2 | OPSWAT Inc. |
| libwamf.sys | 388350 | OPSWAT Inc. |
| SZEDRDrv.sys | 388346 | SaferZone Co. |
| szardrv.sys | 388345 | SaferZone Co. |
| szpcmdrv.sys | 388341 | SaferZone Co. |
| szdfmdrv.sys | 388340 | SaferZone Co. |
| szdfmdrv_usb.sys | 388331 | SaferZone Co. |
| sprtdrv.sys | 388330 | SaferZone Co. |
| SWFsFltrv2.sys | 388321 | Solarwinds LLC |
| SWFsFltr.sys | 388320 | Solarwinds LLC |
| flashaccelfs.sys | 388310 | Network Appliance |
| changelog.sys | 388300 | Network Appliance |
| stcvsm.sys | 388250 | StorageCraft Tech |
| aUpDrv.sys | 388240 | ITSTATION Inc |
| fshs.sys | 388222 | F-Secure |
| fshs.sys | 388221 | F-Secure |
| fsatp.sys | 388220 | F-Secure |
| SecdoDriver.sys | 388210 | Secdo |
| TGFSMF.sys | 388200 | Tetraglyph Technologies |
| napfflti.sys | 388150.5 | NETAND Co Ltd |
| OwlyshieldRansomFilter.sys | 388110.5 | SitinCloud SAS |
| evscase.sys | 388100 | March Hare Software Ltd |
| VSScanner.sys | 388050 | VoodooSoft, LLC |
| HDRansomOffDrv.sys | 388044 | Heilig Defense LLC |
| HDCorrelateFDrv.sys | 388042 | Heilig Defense LLC |
| HDFileMon.sys | 388040 | Heilig Defense LLC |
| tsifilemon.sys | 388012 | Intercom Inc. |
| MarSpy.sys | 388010 | Intercom Inc. |
| AGSysLock.sys | 388002 | AppGuard LLC |
| AGSecLock.sys | 388001 | AppGuard LLC |
| BrnFileLock.sys | 388000 | Blue Ridge Networks |
| BrnSecLock.sys | 387990 | Blue Ridge Networks |
| LCmPrintMon.sys | 387978 | YATEM Co. Ltd. |
| LCgAdMon.sys | 387977 | YATEM Co. Ltd. |
| LCmAdMon.sys | 387976 | YATEM Co. Ltd. |
| LCgFileMon.sys | 387975 | YATEM Co. Ltd. |
| LCmFile.sys | 387974 | YATEM Co. Ltd. |
| LCgFile.sys | 387972 | YATEM Co. Ltd. |
| LCmFileMon.sys | 387970 | YATEM Co. Ltd. |
| IridiumSwitch.sys | 387960 | Confio |
| axfsysmon.sys | 387951 | AppiXoft |
| scensemon.sys | 387950 | AppiXoft |
| ruaff.sys | 387940 | RUNEXY |
| bbfilter.sys | 387930 | derivo GmbH |
| Bfmon.sys | 387920 | Baidu (Hong Kong SAR) Limited |
| bdsysmon.sys | 387912 | Baidu Online Network |
| BdRdFolder.sys | 387910 | Baidu (beijing) |
| mlsaff.sys | 387901 | RUNEXY |
| pscff.sys | 387900 | Weing Co., Ltd. |
| fcnotify.sys | 387880 | TCXA Ltd. |
| aaf.sys | 387860 | Actifio Inc |
| gddcv.sys | 387840 | G Data Software AG |
| wgfile.sys | 387820 | ORANGE WERKS Inc |
| zesfsmf.sys | 387800 | Novell |
| BWAnticheat.sys | 387750 | Binklac Workstation |
| uamflt.sys | 387700 | Sevtechnotrans |
| ehdrv.sys | 387600 | ESET, spol. s r.o. |
| DattoFSF.sys | 387560 | Datto Inc |
| RubrikFileAudit.sys | 387552 | Rubrik Inc |
| FileSystemCBT.sys | 387550 | Rubrik Inc |
| Snilog.sys | 387500 | Systemneeds, Inc |
| tss.sys | 387400 | Tiversa Inc |
| LmDriver.sys | 387390 | in-soft Kft. |
| WDCFilter.sys | 387330 | Interset Inc. |
| altcbt.sys | 387320 | Altaro Ltd. |
| bapfecpt.sys | 387310 | BitArmor Systems, Inc |
| bamfltr.sys | 387300 | BitArmor Systems, Inc |
| TrustedEdgeFfd.sys | 387200 | FileTek, Inc. |
| MRxGoogle.sys | 387100 | Google, Inc. |
| YFSDR.SYS | 387010 | Yokogawa R&L Corp |
| YFSD.SYS | 387000 | Yokogawa R&L Corp |
| YFSRD.sys | 386990 | Yokogawa R&L Corp |
| psgfoctrl.sys | 386990 | Yokogawa R&L Corp |
| psgdflt.sys | 386980 | Yokogawa R&L Corp |
| USBPDH.SYS | 386901 | Centre for Development of Advanced Computing |
| pecfilter.sys | 386900 | C-DAC Hyderabad |
| GKPFCB64.sys | 386810 | INCA Internet Co., Ltd. |
| TkPcFtCb.sys on 32bit | 386800 | INCA Internet Co., Ltd. |
| TkPcFtCb64.sys on 64bit | 386800 | INCA Internet Co., Ltd. |
| bmregdrv.sys | 386731 | Yandex LLC |
| bmfsdrv.sys | 386730 | Yandex LLC |
| CarbonBlackK.sys | 386720 | Bit9 Inc. |
| ScAuthFSFlt2.sys | 386711 | Security Code LLC |
| ScAuthFSFlt.sys | 386710 | Security Code LLC |
| ScAuthIoDrv.sys | 386700 | Security Code LLC |
| mfeaskm.sys | 386610 | McAfee Inc. |
| mfencfilter.sys | 386600 | McAfee |
| WinFLAHdrv.sys | 386540 | NewSoftwares.net, Inc. |
| WinFLAdrv.sys | 386530 | NewSoftwares.net, Inc. |
| WinDBdrv.sys | 386520 | NewSoftwares.net, Inc. |
| WinFLdrv.sys | 386510 | NewSoftwares.net, Inc. |
| WinFPdrv.sys | 386500 | NewSoftwares.net, Inc. |
| varpffmon.sys | 386486 | Varlook Ltd. |
| SkyWPDrv.sys | 386435 | Sky Co., Ltd. |
| SkyRGDrv.sys | 386431 | Sky Co., LTD. |
| SkyAMDrv.sys | 386430 | Sky Co., LTD. |
| SheedSelfProtection.sys | 386421 | SheedSoft Ltd |
| arta.sys | 386420 | SheedSoft Ltd. |
| ApexSqlFilterDriver.sys | 386410 | ApexSQL LLC |
| stflt.sys | 386400 | Xacti |
| tbrdrv.sys | 386390 | Crawler Group |
| WinTeonMiniFilter.sys | 386320 | Dmitry Stefankov |
| wiper.sys | 386310 | Dmitry Stefankov |
| DevMonMiniFilter.sys | 386300 | Dmitry Stefankov |
| VMWVvpfsd.sys | 386200 | VMware, Inc. |
| RTOLogon.sys (Renamed) | 386200 | VMware, Inc. |
| Code42Filter.sys | 386190 | Code42 |
| AATFilter.sys | 386189.5 | Code42 |
| ConduantFSFltr.sys | 386180 | Conduant Corporation |
| KtFSFilter.sys | 386170 | Keysight Technologies |
| FileGuard.sys | 386140 | RES Software |
| NetGuard.sys | 386130 | RES Software |
| RegGuard.sys | 386120 | RES Software |
| ImgGuard.sys | 386110 | RES Software |
| AppGuard.sys | 386100 | RES Software |
| RuiDiskFs.sys | 386030 | RuiGuard Ltd |
| minitrc.sys | 386020 | Protected Networks |
| cpepmon.sys | 386010 | Checkpoint Software |
| CGWMF.sys | 386000 | NetIQ |
| ISRegFlt.sys | 385990 | Flexera Software Inc. |
| ISRegFlt64.sys | 385990 | Flexera Software Inc. |
| shdlpSf.sys | 385970 | Comtrue Technology |
| ctrPAMon.sys | 385960 | Comtrue Technology |
| shdlpMedia.sys | 385950 | Comtrue Technology |
| SealProtect.sys | 385920.7 | Beijing Bytedance |
| FLProtect.sys | 385920.5 | Beijing Volcano Engine |
| immflex.sys | 385910 | Immidio B.V. |
| StegoProtect.sys | 385900 | Stegosystems Inc |
| brfilter.sys | 385890 | Bromium Inc |
| BrCow_x_x_x_x.sys | 385889 | Bromium Inc |
| BemK.sys | 385888 | Bromium Inc |
| secRMM.sys | 385880 | Squadra Technologies, LLC. |
| dgfilter.sys | 385870 | DataGravity Inc. |
| WFP_MRT.sys | 385860 | FireEye Inc |
| EsArtemis.sys | 385855.5 | Elpha Secure Technology Inc. |
| klrsps.sys | 385815 | Kaspersky Lab |
| klsnsr.sys | 385810 | Kaspersky Lab |
| TaniumRecorderDrv.sys | 385800 | Tanium |
| bdsmonsys.sys | 385750 | Binary Defense Systems |
| CdsgFsFilter.sys | 385700 | CRU Data Security Group |
| mssecflt.sys | 385600 | Microsoft |
| Backupreader.sys | 385500 | Microsoft |
| MsixPackagingToolMonitor.sys | 385410 | Microsoft |
| AppVMon.sys | 385400 | Microsoft |
| DpmFilter.sys | 385300 | Microsoft |
| UCPD.sys | 385250.5 | Microsoft |
| ahflt.sys  | 385250.3 | Microsoft |
| SystemInformer.sys | 385210.5 | Winsider Seminars & Solutions, Inc. |
| Procmon11.sys | 385200 | Microsoft |
| wtd.sys | 385110 | Microsoft |
| uberAgentFilter.sys | 385105.5 | vast limits GmbH |
| minispy.sys - Top | 385100 | Microsoft |
| fdrtrace.sys | 385001 | Microsoft |
| filetrace.sys | 385000 | Microsoft |
| uwfreg.sys | 384910 | Microsoft |
| uwfs.sys | 384900 | Microsoft |
| locksmith.sys | 384800 | Microsoft |
| winload.sys | 384700 | Microsoft |
| SFPMonitor.sys - Top | 383350 | SonicWall Inc |
| FilrDriver.sys | 383340 | Micro Focus |
| rwchangedrv.sys | 383330 | Rackware |
| airship-filter.sys | 383320 | AIRWare Technology Ltd |
| AeFilter.sys | 383310 | Faronics Corporation |
| QQProtect.sys | 383300 | Tencent (Shenzhen) |
| QQProtectX64.sys | 383300 | Tencent (Shenzhen) |
| KernelAgent32.sys | 383260 | ZoneFox |
| WRDWIZFILEPROT.SYS | 383251 | WardWiz |
| WRDWIZREGPROT.SYS | 383250 | WardWiz |
| groundling32.sys | 383200 | Dell Secureworks |
| groundling64.sys | 383200 | Dell Secureworks |
| avgtpx86.sys | 383190 | AVG Technologies CZ, s.r.o |
| avgtpx64.sys | 383190 | AVG Technologies CZ, s.r.o |
| DataNow_Driver.sys | 383182 | AppSense Ltd |
| UcaFltDriver.sys | 383180 | AppSense Ltd |
| YFSD2.sys | 383170 | Yokogawa Corpration |
| Kisknl.sys | 383160 | kingsoft |
| MWatcher.sys | 383150 | Neowiz Corporation |
| tsifilemon.sys | 383140 | Intercom Inc. |
| FIM.sys | 383130 | eIQnetworks Inc. |
| cFSfdrv | 383120 | Chaewool |
| ajfsprot.sys | 383110 | Analytik Jena AG |
| isafermon | 383100 | (c)SMS |
| kfac.sys | 383000 | Beijing CA-JinChen Software Co., Ltd |
| GUMHFilter.sys | 382910 | Glarysoft Ltd. |
| PsAcFileAccessFilter.sys | 382902 | FUJITSU SOFTWARE |
| FJGSDis2.sys | 382900 | FUJITSU LIMITED |
| secure_os.sys | 382890 | FUJITSU LIMITED |
| ibr2fsk.sys | 382880 | FUJITSU ENGINEERING |
| FJSeparettiFilterRedirect.sys | 382860 | FUJITSU LIMITED |
| Fsw31rj1.sys | 382855 | FUJITSU LIMITED |
| da_ctl.sys | 382850 | FUJITSU LIMITED |
| zqFilter.sys | 382800 | magrasoft Ltd |
| ntps_fa.sys | 382700 | DefendX Software |
| ancfunc.sys | 382650 | Aunaki |
| sConnect.sys | 382600 | I-O DATA DEVICE, INC |
| AdaptivaClientCache32.sys | 382500 | Adaptiva |
| AdaptivaclientCache64.sys | 382500 | Adaptiva |
| phantomd.sys | 382440 | Veramine Inc |
| GoFSMF.sys | 382430 | Gorizonty Rosta Ltd |
| SWCommFltr.sys | 382420 | SnoopWall LLC |
| atflt.sys | 382410 | Atlansys Software, LLC |
| amfd.sys | 382400 | Atlansys Software, LLC |
| iSafeKrnl.sys | 382390 | Elex Tech Inc |
| iSafeKrnlMon.sys | 382380 | Elex Tech Inc |
| EdrDriver.sys | 382350.5 | Huawei Technologies Co. Ltd. |
| AtdrAgent.sys | 382325 | 360 Software (Beijing) |
| AtdrAgent64.sys | 382325 | 360 Software (Beijing) |
| Qutmdrv.sys | 382320 | 360 Software (Beijing) |
| 360box.sys | 382310 | Qihoo 360 |
| 360fsflt.sys | 382300 | Beijing Qihoo Technology Co., Ltd. |
| PSFSF.sys | 382250.5 | Peer Software Inc |
| scred.sys | 382210 | SoftCamp Co., Ltd. |
| PDGenFam.sys | 382200 | Soluto LTD |
| MCFileMon64.sys (x64 systems) | 382100 | Sumitomo Electric Ltd. |
| MCFileMon32.sys (x32 systems) | 382100 | Sumitomo Electric Ltd. |
| RyGuard.sys | 382050 | SHENZHEN UNNOO Information Techco., Ltd |
| FileShareMon.sys | 382040 | SHENZHEN UNNOO Information Techco., Ltd |
| ryfilter.sys | 382030 | SHENZHEN UNNOO Information Techco., Ltd |
| secufile.sys | 382020 | Shenzhen Unnoo LTD |
| XiaobaiFs.sys | 382010 | Shenzhen Unnoo LTD |
| XiaobaiFsR.sys | 382000 | Shenzhen Unnoo LTD |
| TWBDCFilter.sys | 381910 | Trustwave |
| VPDrvNt.sys | 381900 | AhnLab, Inc. |
| eetd32.sys | 381800 | Entrust Inc. |
| eetd64.sys | 381800 | Entrust Inc. |
| dnaFSMonitor.sys | 381700 | Dtex Systems |
| iwhlp2.sys on 2000 | 381610 | InfoWatch |
| iwhlpxp.sys on XP | 381610 | InfoWatch |
| iwhlp.sys on Vista | 381610 | InfoWatch |
| iwdmfs.sys | 381600 | InfoWatch |
| IronGateFD.sys | 381500 | rubysoft |
| MagicBackupMonitor.sys | 381400 | Magic Softworks, Inc. |
| Sonar.sys | 381337 | IKARUS Security |
| IPFilter.sys | 381310 | Jinfengshuntai |
| MSpy.sys | 381300 | Ladislav Zezula |
| inuse.sys | 381200 | March Hare Software Ltd |
| qfmon.sys | 381190 | Quality Corporation |
| FMSRVCIO.sys | 381165 | NEC Solution Innovators |
| flyfs.sys | 381160 | NEC Soft, Ltd. |
| serfs.sys | 381150 | NEC Soft, Ltd. |
| hdrfs.sys | 381140 | NEC Soft, Ltd. |
| UVMCIFSF.sys | 381130 | NEC Corporation |
| ICFClientFlt.sys | 381120 | NEC System Technologies, Ltd. |
| IccFileIoAd.sys | 381110 | NEC System Technologies, Ltd. |
| IccFilterAudit.sys | 381100 | NEC System Technologies |
| IccFilterSc.sys | 381090 | InfoCage |
| Sefo.sys - Top | 381010 | Solusseum Inc |
| mtsvcdf.sys | 381000 | CristaLink |
| SDDrvLdr.sys | 380970 | Aliaksander Lebiadzevich |
| fscbtflt.sys | 380930.5 | Cohesity Inc |
| SQLsafeFilterDriver.sys | 380901 | Idera Software |
| IderaFilterDriver.sys | 380900 | Idera |
| sie-filemon.sys | 380852.5 | SN Systems Ltd |
| cbfilter20.sys | 380852 | SN Systems Ltd |
| cbfsfilter2017.sys | 380850 | SN Systems Ltd |
| xhunter1.sys | 380800 | Wellbia.com |
| iGuard.sys | 380720 | i-Guard SAS |
| cbfltfs4.sys | 380715 | Nomadesk |
| cbfltfs4.sys | 380710 | Backup Systems Ltd |
| PkgFilter.sys | 380700 | Scalable Software Inc. |
| Itff.sys | 380670.5 | Light Star Information |
| minifswatcher.sys | 380650 | BITCORP S.R.L. |
| snimg.sys | 380600 | Softnext Technologies |
| cbfilter20.sys | 380530 | Brainloop AG |
| SK.sys | 380520 | HEAT Software |
| cbfsfilter2017.sys | 380515 | Kits Ltd. |
| mpxmon.sys | 380510 | Positive Technologies |
| filenamevalidator.sys | 380502 | Infotecs |
| SWAgent.sys | 380500.5 | Stairwell Inc |
| KC3.sys | 380500 | Infotecs |
| PLPOffDrv.sys | 380492 | SK Infosec Co |
| ISFPDrv.sys | 380491 | SK Infosec Co |
| ionmonwdrv.sys | 380490 | SK Infosec Co |
| Sefo.sys - Middle | 380480 | Solusseum Inc |
| sagntflt.sys | 380470 | ShinNihonSystec Co |
| VrVBRFsFilter.sys | 380461 | Hauri Inc |
| VrExpDrv.sys | 380460 | Hauri Inc |
| srminifilterdrv.sys | 380450 | Citrix Systems |
| zzpensys.sys | 380440 | Zhuan Zhuan Jing Shen |
| tedrdrv.sys | 380430 | Palo Alto Networks |
| fangcloud_autolock_driver.sys | 380420 | Hangzhou Yifangyun |
| FASDriver | 380410 | Tech Research |
| kFileFlt.sys | 380405 | AsiaInfo Technologies |
| cpfd10.sys | 380400 | CYEBIZ co Ltd |
| ZeroneAODVirtualDisk.sys | 380390.5 | Zero One Technology Co |
| ZeroneAODVirtualDisk64.sys | 380390.5 | Zero One Technology Co |
| edrmon.sys | 380050.5 | CELALETTIN ER |
| edrsec.sys | 380050.5 | CELALETTIN ER |
| edrfrm.sys | 380050.5 | CELALETTIN ER |
| edrprt.sys | 380050.5 | CELALETTIN ER |
| edrhips.sys | 380050.5 | CELALETTIN ER |
| CbSampleDrv.sys | 380020 | Microsoft |
| CbSampleDrv.sys | 380010 | Microsoft |
| CbSampleDrv.sys | 380000 | Microsoft |
| SlrRegFlt.sys | 375000.8 | AST Cyber Lab LLP |
| SlrFsFlt.sys | 375000.5 | AST Cyber Lab LLP |
| EdsAppRep.sys | 372000.5 | Alibaba Cloud Computing Ltd. |
| simrep.sys | 371100 | Microsoft |
| change.sys | 370160 | Microsoft |
| delete_flt.sys | 370150 | Microsoft |
| SmbResilFilter.sys | 370140 | Microsoft |
| usbtest.sys | 370130 | Microsoft |
| NameChanger.sys | 370120 | Microsoft |
| failMount.sys | 370110 | Microsoft |
| failAttach.sys | 370100 | Microsoft |
| stest.sys | 370090 | Microsoft |
| cdo.sys | 370080 | Microsoft |
| ctx.sys | 370070 | Microsoft |
| fmm.sys | 370060 | Microsoft |
| cancelSafe.sys | 370050 | Microsoft |
| message.sys | 370040 | Microsoft |
| passThrough.sys | 370030 | Microsoft |
| nullFilter.sys | 370020 | Microsoft |
| ntest.sys | 370010 | Microsoft |
| minispy.sys - Middle | 370000 | Microsoft |
| VersaTamperProtectionDriver.sys | 369650.5 | Versa Networks Inc. |
| KenestoDriveAC.sys | 369620.5 | Kenesto Corp |
| ZdProtect.sys | 369600.5 | Chongqing Intelligent Information Tech Co.,Ltd |
| MEDrv.sys | 369565.5 | mistiny.com |
| cbfilter20.sys | 369560.5 | Blondell-Hart Inc. |
| CyberhavenSystemMonitor.sys | 368550.5 | Cyberhaven Inc |
| AvaPsFD.sys | 368540 | Avanite Limited |
| isecureflt.sys | 368530 | iSecure Ltd. |
| SFPMonitor.sys - Middle | 368520 | SonicWall Inc |
| wats_se.sys | 368510 | Fujian Shen Kong |
| secure_os_mf.sys | 368500 | HAURI |
| FileMonitor.sys | 368470 | Cygna Labs |
| asiofms.sys | 368460 | Encourage Technologies |
| AbtFileSystemBlocker.sys | 368452 | Absolute Software |
| cbfsfilter2017.sys | 368450 | Absolute Software |
| FileHubAgent.sys | 368440 | SmartFile LLC |
| pfracdrv.sys | 368430 | NURILAB |
| nrcomgrdki.sys | 368420 | NURILAB |
| nrcomgrdka.sys | 368420 | NURILAB |
| nrpmonki.sys | 368410 | NURILAB |
| nrpmonka.sys | 368410 | NURILAB |
| nravwka.sys | 368400 | NURILAB |
| bhkavki.sys | 368390 | NURILAB |
| bhkavka.sys | 368390 | NURILAB |
| docvmonk.sys | 368380 | NURILAB |
| docvmonk64.sys | 368380 | NURILAB |
| InvProtectDrv.sys | 368370 | Invincea |
| InvProtectDrv64.sys | 368370 | Invincea |
| browserMon.sys | 368360 | Adtrustmedia |
| SfdFilter.sys | 368350 | Sandoll Communication |
| phdcbtdrv.sys | 368340 | PHD Virtual Tech Inc. |
| sysdiag.sys | 368330 | HeroBravo Technology |
| wlminisecmod.sys | 368329 | Winicssec Ltd |
| WntGPDrv.sys | 368327 | Winicssec Ltd |
| edrdrv.sys | 368325 | Nurd Yazilim A.S. |
| CmdCwagt.sys | 368322 | Comodo Security Solutions Inc. |
| cfrmd.sys | 368320 | Comodo Security Solutions Inc. |
| repdrv.sys | 368310 | Vision Solutions |
| repmon.sys | 368300 | Vision Solutions |
| cvofflineFlt32.sys | 368200 | Quantum Corporation. |
| cvofflineFlt64.sys | 368200 | Quantum Corporation. |
| DsDriver.sys | 368100 | Warp Disk Software |
| xdrmon.sys | 368050.5 | LLC Breakthrough Technologies |
| nlcbhelpx86.sys | 368000 | NetLib |
| nlcbhelpx64.sys | 368000 | NetLib |
| nlcbhelpi64.sys | 368000 | NetLib |
| wbfilter.sys | 367950 | Whitebox Security |
| LRAgentMF.sys | 367900 | LogRhythm Inc. |
| Drwebfwflt.sys | 367810 | Doctor Web |
| EventMon.sys | 367800 | Doctor Web |
| dsfltfs.sys | 367760 | Digitalsense Co |
| soidriver.sys | 367750 | Sophos Plc |
| drvhookcsmf.sys | 367700 | GrammaTech, Inc. |
| drvhookcsmf_amd64.sys | 367700 | GrammaTech, Inc. |
| RevoNetDriver.sys | 367650 | J's Communication Co. |
| avipbb.sys | 367600 | Avira GmbH |
| FileSightMF.sys | 367500 | PA File Sight |
| csaam.sys | 367400 | Cisco Systems |
| FSMon.sys | 367300 | 1mill |
| AccessValidator.sys | 367200 | Shanghai YiCun Network Tech Co. Ltd |
| filefilter.sys | 367100 | Beijing Zhong Hang Jiaxin Computer Technology Co., Ltd. |
| iiscache.sys | 367000 | Microsoft |
| nowonmf.sys | 366993 | Diskeeper Corporation |
| dktlfsmf.sys | 366992 | Diskeeper Corporation |
| DKDrv.sys | 366991 | Diskeeper Corporation |
| DKRtWrt.sys - temp fix for XPSP3 | 366990 | Diskeeper Corporation |
| HBFSFltr.sys | 366980 | Diskeeper Corporation |
| xoiv8x64.sys | 366940 | Arcserve |
| xomfcbt8x64.sys | 366930 | CA |
| KmxAgent.sys | 366920 | CA |
| KmxFile.sys | 366910 | CA |
| KmxSbx.sys | 366900 | CA |
| PointGuardVistaR32.sys | 366810 | Futuresoft |
| PointGuardVistaR64.sys | 366810 | Futuresoft |
| PointGuardVistaF.sys | 366800 | Futuresoft |
| PointGuardVista64F.sys | 366800 | Futuresoft |
| vintmfs.sys | 366789 | CondusivTechnologies |
| hiofs.sys | 366782 | Condusiv Technologies |
| intmfs.sys | 366781 | CondusivTechnologies |
| excfs.sys | 366780 | CondusivTechnologies |
| zampit_ml.sys | 366700 | Zampit |
| CGProtect.sys | 366669.9 | Tencent Technology |
| ProximaGameAntiCheat.sys | 366669.8 | PROXIMA BETA PTE |
| ProximaGameAntiCheat.sys | 366669.7 | PROXIMA BETA PTE |
| ACE-BASE.sys | 366669.6 | Tencent Technology |
| ACE-GAME.sys | 366669.5 | Tencent Technology |
| TenRSafe2.sys | 366669 | Tencent Technology |
| tesxporter.sys | 366667 | Tencent Technology |
| tesxnginx.sys | 366666 | Tencent Technology |
| detector.sys | 366620.5 | MemCrypt Limited |
| rflog.sys | 366600 | AppStream, Inc. |
| csmon.sys | 366582 | CyberSight Inc |
| mumdi.sys | 366540 | ZenmuTech Inc. |
| LivedriveFilter.sys | 366500 | Livedrive Internet Ltd |
| regmonex.sys | 366410 | Tranxition Corp |
| TXRegMon.sys | 366400 | Tranxition Corp |
| SDVFilter.sys | 366300 | Soliton Systems K.K. |
| eLock2FSCTLDriver.sys | 366210 | Egis Technology Inc. |
| msiodrv4.sys | 366200 | Centennial Software Ltd |
| mmPsy32.sys | 366110 | Resplendence Software Projects |
| mmPsy64.sys | 366110 | Resplendence Software Projects |
| rrMon32.sys | 366100 | Resplendence Software Projects |
| rrMon64.sys | 366100 | Resplendence Software Projects |
| cvsflt.sys | 366000 | March Hare Software Ltd |
| ktsyncfsflt.sys | 365920 | KnowledgeTree Inc. |
| nvmon.sys | 365900 | NetVision, Inc. |
| SnDacs.sys | 365810 | Informzaschita |
| SnExequota.sys | 365800 | Informzaschita |
| llfilter.sys | 365700 | SecureAxis Software |
| hafsnk.sys | 365660 | HA Unix Pt |
| DgeDriver.sys | 365655 | Dell Software Inc. |
| BWFSDrv.sys | 365650 | Quest Software Inc. |
| CAADFlt.sys | 365601 | Quest Software Inc. |
| QFAPFlt.sys | 365600 | Quest Software |
| XendowFLT.sys | 365570 | Credant Technologies |
| fmdrive.sys | 365500 | Cigital, Inc. |
| EGMinFlt.sys | 365400 | WhiteCell Software Inc. |
| ddapm.sys | 365355.5 | Datadog |
| it2reg.sys | 365315 | Soliton Systems |
| it2drv.sys | 365310 | Soliton Systems |
| solitkm.sys | 365300 | Soliton Systems |
| pgpwdefs.sys | 365270 | Symantec |
| GEProtection.sys | 365260 | Symantec |
| diflt.sys | 365260 | Symantec Corp. |
| sysMon.sys | 365250 | Symantec |
| ssrfsf.sys | 365210 | Symantec |
| emxdrv2.sys | 365200 | Symantec |
| reghook.sys | 365150 | Symantec |
| spbbcdrv.sys | 365100 | Symantec |
| bhdrvx86.sys | 365100 | Symantec |
| bhdrvx64.sys | 365100 | Symantec |
| symevnt.sys | 365090 | Broadcom |
| symevnt32.sys | 365090 | Broadcom |
| SISIPSFileFilter | 365010 | Symantec |
| symevent.sys | 365000 | Symantec |
| BHDrvx64.sys | 364970 | NortonLifeLock Inc |
| BHDrvx86.sys | 364970 | NortonLifeLock Inc |
| symevnt.sys | 364960 | NortonLifeLock Inc |
| symevnt32.sys | 364960 | NortonLifeLock Inc |
| SymEvent.sys | 364950 | NortonLifeLock Inc |
| wrpfv.sys | 364900 | Microsoft |
| UpGuardRealTime.sys | 364810 | UpGuard |
| usbl_ifsfltr.sys | 364800 | SecureAxis |
| ntfsf.sys | 364700 | Sun&Moon Rise |
| BssAudit.sys | 364600 | ByStorm |
| GPMiniFIlter.sys | 364500 | Kalpataru |
| AlfaFF.sys | 364400 | Alfa |
| 360disproc.sys | 364310.5 | 360 Software (Beijing) |
| FSAFilter.sys | 364300 | ScriptLogic |
| GcfFilter.sys | 364200 | GemacmbH |
| FFCFILT.SYS | 364100 | FFC Limited |
| msnfsflt.sys | 364000 | Microsoft |
| mblmon.sys | 363900 | Packeteer |
| amsfilter.sys | 363800 | Axur Information Sec. |
| rswctrl.sys | 363713 | Douzone Bizon Co |
| mcstrg.sys | 363712 | Douzone Bizon Co |
| fmkkc.sys | 363711 | Douzone Bizon Co |
| nmlhssrv01.sys | 363710 | Douzone Bizon Co |
| equ8_helper.sys | 363705 | Int3 Software AB |
| strapvista.sys (retired) | 363700 | AvSoft Technologies |
| SAFE-Agent.sys | 363636 | SAFE-Cyberdefense |
| EstPrmon.sys | 363610 | ESTsoft corp. |
| Estprp.sys - 64bit | 363610 | ESTsoft corp. |
| EstRegmon.sys | 363600 | ESTsoft corp. |
| EstRegp.sys - 64bit | 363600 | ESTsoft corp. |
| EMAC-Driver-x64.sys | 363570 | EMAC LAB |
| HuntMon.sys | 363558.5 | Huntress Labs Inc |
| agfsmon.sys | 363530 | TechnoKom Ltd. |
| NlxFF.sys | 363520 | OnGuard Systems LLC |
| Sahara.sys | 363511 | Safend |
| Santa.sys | 363510 | Safend |
| vfdrv.sys | 363500 | Viewfinity |
| topdogfsfilt.sys | 363450 | ManTech |
| mamflt.sys | 363430 | Mirekusoft LLC |
| sfac.sys | 363420 | SoulFrost |
| xhunter64.sys | 363400 | Wellbia.com |
| uncheater.sys | 363390 | Wellbia.com |
| AuditFlt.sys | 363313 | Ionx Solutions LLP |
| SPIMiniFilter.sys | 363300 | Software Pursuits Inc. |
| EAAntiCheat.sys | 363250 | Electronic Arts |
| RevBitsESMF.sys | 363240.5 | RevBits LLC |
| mracdrv.sys | 363230 | Mail&#x2024;Ru |
| BEDaisy.sys | 363220 | BattlEye Innovations |
| MPKernel.sys | 363210 | Lovelace Network Tech |
| NetAccCtrl.sys | 363200 | LINK co., ltd |
| NetAccCtrl64.sys | 363200 | LINK co., ltd |
| bzsenedrsysdrv.sys | 363143 | BiZone LLC |
| bzsenyaradrv.sys | 363142 | BiZone LLC |
| bzsenspdrv.sys | 363141 | BiZone LLC |
| bzsenth.sys | 363140 | BiZone LLC |
| hpreg.sys | 363130 | HP |
| QMON.sys | 363122 | Qualys Inc. |
| qfimdvr.sys | 363120 | Qualys Inc. |
| QDocumentREF.sys | 363110 | BicDroid Inc. |
| dsfemon.sys | 363100 | Topology Ltd |
| zdpinfrastructure.sys | 363040.5 | Zscaler Inc. |
| AmznMon.sys | 363030 | Amazon Web Services Inc |
| iothorfs.sys | 363020 | ioScience |
| ctamflt.sys | 363010 | ComTrade |
| psisolator.sys | 363000 | SharpCrafters |
| QmInspec.sys | 362990 | Beijing QiAnXin Tech. |
| HVLMinifilter.sys | 362980 | HAVELSAN A.Åž |
| GagSecurity.sys | 362970 | Beijing Shu Yan Science |
| vfpd.sys | 362962 | CyberArk Software |
| CybKernelTracker.sys | 362960 | CyberArk Software |
| filemon.sys | 362950 | Temasoft S.R.L. |
| SCAegis.sys | 362940 | Sogou Ltd. |
| fpepflt.sys | 362930 | ForcePoint LLC. |
| GTVService.sys | 362920 | GTV VIETNAM TECHNOLOGY |
| RWLog1.sys | 362910.5 | ROMWin Co. Ltd |
| klifks.sys | 362902 | Kaspersky Lab |
| klifaa.sys | 362901 | Kaspersky Lab |
| Klifsm.sys | 362900 | Kaspersky Lab |
| lwdcs.sys | 362880.5 | Lacework Inc |
| Spotlight.sys | 362870 | Cigent Technology Inc |
| nxrmflt.sys | 362860 | NextLabs, Inc. |
| vast.sys | 362850 | ReliaQuest |
| AALProtect.sys | 362840 | AlphaAntiLeak |
| egnfsflt.sys | 362830 | Egnyte Inc |
| RsFlt.sys | 362820 | Redstor Limited |
| CentrifyFSF.sys | 362810 | Centrify Corp |
| Sefo.sys - Bottom | 362800 | Solusseum Inc |
| proggerdriver.sys | 362790 | WaikatoLink Ltd |
| imfilter.sys | 362780 | ITsMine |
| webargus.sys | 362775.5 | Digital Information Technologies |
| DSHSM.sys | 362770.5 | DeepSpace Storage Systems |
| GraphiteSecureDriver.sys | 362750.5 | Towers Watson Software |
| IndigoSecureDriver.sys | 362750 | Towers Watson Software |
| SFPMonitor.sys - Bottom | 362700 | SonicWall Inc |
| ceecava.sys | 361010.5 | Dell Technologies Inc. |
| minispy.sys - Bottom | 361000 | Microsoft |

## 340000 - 349999: FSFilter Undelete

| Minifilter                  | Altitude | Company                                 |
|-----------------------------|----------|-----------------------------------------|
| LookoutAccessProtection.sys | 347000.5 | Lookout |
| BSSFlt.sys | 346000 | Blue Shoe Software LLC |
| ThinIO.sys | 345900 | ThinScale Technology |
| hmpalert.sys | 345800 | SurfRight |
| nsffkmd64.sys | 345700 | NetSTAR Inc. |
| nsffkmd32.sys | 345700 | NetSTAR Inc. |
| xbprocfilter.sys | 345600 | Zrxb |
| ifileguard.sys | 345500 | I-O DATA DEVICE, INC. |
| undelex32.sys | 345400 | Resplendence Software Projects |
| undelex64.sys | 345400 | Resplendence Software Projects |
| starmon.sys | 345300 | Kantowitz Engineering, Inc. |
| mxRCycle.sys | 345200 | Avanquest |
| UdFilter.sys | 345100 | Diskeeper Corporation |
| it2prtc.sys | 345040 | Soliton Systems K.K. |
| SolRegFilter.sys | 345030 | Soliton Systems K.K. |
| SolSecBr.sys | 345020 | Soliton Systems K.K. |
| SolFCLLi.sys | 345010 | Soliton Systems K.K. |
| WinSetupMon.sys | 345102 | Microsoft |
| SolFCL.sys | 345000 | Soliton Smart Sec |
| DCVPr.sys | 340700 | SecurStar GmbH |

## 320000 - 329998: FSFilter Anti-Virus

| Minifilter                  | Altitude | Company                                 |
|-----------------------------|----------|-----------------------------------------|
| brynhildr.sys | 329400 | Activision Blizzard, Inc. |
| IstroDrv.sys | 329380.5 | IstroSec s.r.o. |
| XRFilter.sys | 329375 | XRITDX |
| tbmninifilter.sys | 329370 | Confluera Inc |
| CovAgent.sys | 329365 | Field Effect Software |
| trfsfilter.sys | 329360 | NetSecurity Corp |
| SentinelMonitor.sys | 329355.5 | SentinelOne, Inc. |
| ReveFltMgr.sys | 329350 | REVE Antivirus |
| MagicArmorDrv.sys | 329345.5 | Beijing VEDA Information Technology Co. Ltd |
| ReveProcProtection.sys | 329340 | REVE Antivirus |
| zwPxeSvr.sys | 329330 | SecureLink Inc. |
| zwASatom.sys | 329320 | SecureLink Inc. |
| wscm.sys | 329310 | FUJITSU LIMITED |
| IMFFilter.sys | 329300 | IObit Information Tech |
| CSFlt.sys | 329290 | ConeSecurity Inc |
| cfcdrv_unloadable.sys | 329270.5 | eSentire Inc |
| PWProtect.sys | 329250 | PerfectWorld Ltd |
| Osiris.sys | 329240 | Binary Defense Systems |
| ospfile_mini.sys | 329230 | OKUMA Corp |
| SoftFilterxxx.sys | 329222 | WidgetNuri Corp |
| RansomDefenseCert.sys | 329220.5 | WidgetNuri Corp |
| RansomDefensexxx.sys | 329220 | WidgetNuri Corp |
| RanPodFS.sys | 329210 | Pooyan System |
| ksfsflt.sys | 329200 | Beijing Kingsoft |
| DeepInsFS.sys | 329190 | Deep Instinct |
| AppCheckD.sys | 329180 | CheckMAL Inc |
| spellmon.sys | 329170 | SpellSecurity |
| WhiteShield.sys | 329160 | Meidensha Corp |
| reaqtor.sys | 329150 | ReaQta Ltd. |
| SE46Filter.sys | 329140 | Technology Nexus AB |
| FileScan.sys | 329130 | NPcore Ltd |
| ECATDriver.sys | 329120 | EMC |
| pfkrnl.sys | 329110 | FXSEC LTD |
| epicFilter.sys | 329100 | Hidden Reflex |
| EdnemFsFilter.sys | 329090 | Dakota State University |
| b9kernel.sys | 329050 | Bit9 Inc |
| AGR.sys | 329040.5 | Agger Labs Ltd. |
| WdDevFlt.sys | 329030 | Microsoft |
| eeCtrl.sys | 329010 | symantec |
| eraser.sys (Retired) | 329010 | symantec |
| SRTSP.sys | 329000 | symantec |
| SRTSPIT.sys - ia64 systems | 329000 | symantec |
| SRTSP64.SYS - x64 systems | 329000 | symantec |
| eeCtrl.sys | 328960 | NortonLifeLock Inc |
| SRTSP.sys | 328950 | NortonLifeLock Inc |
| SRTSP64.sys | 328950 | NortonLifeLock Inc |
| a2ertpx86.sys | 328920 | Emsi Software GmbH |
| a2ertpx64.sys | 328920 | Emsi Software GmbH |
| a2gffx86.sys - x86 | 328910 | Emsi Software GmbH |
| a2gffx64.sys - x64 | 328910 | Emsi Software GmbH |
| a2gffi64.sys - IA64 | 328910 | Emsi Software GmbH |
| a2acc.sys | 328900 | Emsi Software GmbH |
| a2acc64.sys on x64 systems | 328900 | Emsi Software GmbH |
| eppfilebackup.sys | 328890.5 | Emsisoft Ltd. |
| FlightRecorder.sys | 328850 | Malwarebytes Corp. |
| upfilt.sys | 328820.5 | Upsight Security |
| si32_file.sys | 328810 | Scargo Inc |
| si64_file.sys | 328810 | Scargo Inc |
| mbam.sys | 328800 | Malwarebytes Corp. |
| lnvscenter.sys | 328780 | Lenovo |
| EnigmaFileMonDriver.sys | 328770 | EnigmaSoft |
| KUBWKSP.sys | 328750 | Netlor SAS |
| hcp_kernel_acq.sys | 328740 | refractionPOINT |
| SegiraFlt.sys | 328730 | Segira LLC |
| wdocsafe.sys | 328722 | Cheetah Mobile Inc. |
| lbprotect.sys | 328720 | Cheetah Mobile Inc. |
| eamonm.sys | 328700 | ESET, spol. s r.o. |
| snpavdrv.sys | 328660 | Security Code LLC |
| klam.sys | 328650 | Kaspersky Lab |
| MaxProc64.sys | 328620 | Max Secure Software |
| MaxProtector.sys | 328610 | Max Secure Software |
| maxcryptmon.sys | 328601 | Max Secure Software |
| SDActMon.sys | 328600 | Max Secure Software |
| TmKmSnsr.sys | 328550 | Trend Micro Inc. |
| fileflt.sys | 328540 | Trend Micro Inc. |
| TmEsFlt.sys | 328530 | Trend Micro Inc. |
| TmEyes.sys | 328520 | Trend Micro Inc. |
| tmevtmgr.sys | 328510 | Trend Micro Inc. |
| tmpreflt.sys | 328500 | Trend |
| vcMFilter.sys | 328400 | SGRI Co., LTD. |
| SAFsFilter.sys | 328300 | Lightspeed Systems Inc. |
| vsepflt.sys | 328200 | VMware, Inc. |
| VFileFilter.sys(renamed) | 328200 | VMware, Inc. |
| sfavflt.sys | 328130 | Sangfor Technologies |
| sfavflt.sys | 328120 | Sangfor Technologies |
| drivesentryfilterdriver2lite.sys | 328100 | DriveSentry Inc |
| WdFilter.sys | 328010 | Microsoft |
| mpFilter.sys | 328000 | Microsoft |
| vrSDetri.sys | 327801 | ETRI |
| vrSDetrix.sys | 327800 | ETRI |
| AhkSvPro.sys | 327720 | Ahkun Co., Ltd. |
| AhkUsbFW.sys | 327710 | Ahkun Co., Ltd. |
| AhkAMFlt.sys | 327700 | Ahkun Co., Ltd. |
| majoradvapi.sys | 327680 | Beijing Majorsec |
| PSINPROC.SYS | 327620 | Panda Security |
| PSINFILE.SYS | 327610 | Panda Security |
| amfsm.sys - Windows XP/2003 x64 | 327600 | Panda Security |
| amm8660.sys - Windows Vista x86 | 327600 | Panda Security |
| amm6460.sys - Windows Vista x64 | 327600 | Panda Security |
| PerfectWorldAntiCheatSys.sys | 327560 | Perfect World Co. Ltd |
| ADSpiderDoc.sys | 327550 | Digitalonnet |
| BkavAutoFlt.sys | 327542 | Bkav Corporation |
| BkavSdFlt.sys | 327540 | Bkav Corporation |
| easyanticheat.sys | 327530 | EasyAntiCheat Solutions |
| 5nine.cbt.sys | 327520 | 5nine Software Inc. |
| caavFltr.sys | 327510 | Computer Assoc |
| ino_fltr.sys | 327500 | Computer Assoc |
| SECOne_USB.sys | 327426 | GRGBanking Equipment |
| SECOne_Proc10.sys | 327424 | GRGBanking Equipment |
| SECOne_REG10.sys | 327422 | GRGBanking Equipment |
| SECOne_FileMon10.sys | 327420 | GRGBanking Equipment |
| WCSDriver.sys | 327410 | White Cloud Security |
| 360qpesv.sys | 327404 | 360 Software (Beijing) |
| dsark.sys | 327402 | Qihoo 360 |
| 360avflt.sys | 327400 | Qihoo 360 |
| sciptflt.sys | 327334 | SECUI Corporation |
| scifsflt.sys | 327333 | SECUI Corporation |
| ANVfsm.sys | 327310 | Arcdo |
| CDrRSFlt.sys | 327300 | Arcdo |
| mfdriver.sys | 327250 | Imperva Inc. |
| EPSMn.sys | 327200 | SGA |
| TxFileFilter.sys | 327160 | Beijing Venus |
| VTSysFlt.sys | 327150 | Beijing Venus |
| TesMon.sys | 327130 | Tencent |
| QQSysMonX64.sys | 327125 | Tencent |
| QQSysMon.sys | 327120 | Tencent |
| TSysCare.sys | 327110 | Shenzhen Tencent Computer Systems Company Limited |
| TFsFlt.sys | 327100 | Shenzhen Tencent Computer Systems Company Limited |
| avmf.sys | 327000 | Authentium |
| BDFileDefend.sys | 326916 | Baidu (beijing) |
| BDsdKit.sys | 326914 | Baidu online network technology (beijing)Co., Ltd |
| bd0003.sys | 326912 | Baidu online network technology (beijing)Co., Ltd |
| Bfilter.sys | 326910 | Baidu (Hong Kong SAR) Limited |
| NeoKerbyFilter | 326900 | NeoAutus |
| egnfsflt.sys | 326830 | Egnyte Inc |
| RsFlt.sys | 326820 | Redstor Limited |
| trpmnflt.sys | 326810 | TRAPMINE A.S. |
| PLGFltr.sys | 326800 | Paretologic |
| WrdWizSecure64.sys | 326730 | WardWiz |
| wrdwizscanner.sys | 326720 | WardWiz |
| AshAvScan.sys | 326700 | Ashampoo GmbH & Co. KG |
| Zyfm.sys | 326666 | ZhengYong InfoTech LTD. |
| csaav.sys | 326600 | Cisco Systems |
| oavfm.sys | 326550 | HSM IT-Services Gmbh |
| SegMD.sys | 326520 | Segurmatica |
| SegMP.sys | 326510 | Segurmatica |
| SegF.sys | 326500 | Segurmatica |
| eeyehv.sys | 326400 | eEye Digital Security |
| eeyehv64.sys | 326400 | eEye Digital Security |
| CpAvFilter.sys | 326311 | CodeProof Technologies Inc |
| CpAvKernel.sys | 326310 | CodeProof Technologies Inc |
| NovaShield.sys | 326300 | Securitas Technologies, Inc. |
| SheedAntivirusFilterDriver.sys | 326290 | SheedSoft Ltd |
| bSyirmf.sys | 326260 | BLACKFORT SECURITY |
| bSysp.sys | 326250 | BLACKFORT SECURITY |
| bSydf.sys | 326240 | BLACKFORT SECURITY |
| bSywl.sys | 326235 | BLACKFORT SECURITY |
| bSyrtm.sys | 326230 | BLACKFORT SECURITY |
| bSyaed.sys | 326220 | BLACKFORT SECURITY |
| bSyar.sys | 326210 | BLACKFORT SECURITY |
| BdFileSpy.sys | 326200 | BullGuard |
| npxgd.sys | 326160 | INCA Internet Co., Ltd |
| npxgd64.sys | 326160 | INCA Internet Co., Ltd |
| tkpl2k.sys | 326150 | INCA Internet Co., Ltd |
| tkpl2k64.sys | 326150 | INCA Internet Co., Ltd |
| GKFF.sys | 326140 | INCA Internet Co., Ltd |
| GKFF64.sys | 326140 | INCA Internet Co., Ltd |
| tkdac2k.sys | 326130 | INCA Internet Co., Ltd |
| tkdacxp.sys | 326130 | INCA Internet Co., Ltd |
| tkdacxp64.sys | 326130 | INCA Internet Co., Ltd |
| tksp2k.sys | 326120 | INCA Internet Co., Ltd |
| tkspxp.sys | 326120 | INCA Internet Co., Ltd |
| tkspxp64.sys | 326120 | INCA Internet Co., Ltd |
| tkfsft.sys | 326110 | INCA Internet Co., Ltd |
| tkfsft64.sys - 64bit | 326110 | INCA Internet Co., Ltd |
| tkfsavxp.sys - 32bit | 326100 | INCA Internet Co., Ltd |
| tkfsavxp64.sys - 64bit | 326100 | INCA Internet Co., Ltd |
| SMDrvNt.sys | 326040 | AhnLab, Inc. |
| ATamptNt.sys | 326030 | AhnLab, Inc. |
| V3Flt2k.sys | 326020 | AhnLab, Inc. |
| V3MifiNt.sys | 326010 | Ahnlab |
| V3Ift2k.sys | 326000 | Ahnlab |
| V3IftmNt.sys (Old name) | 326000 | Ahnlab |
| ArfMonNt.sys | 325990 | Ahnlab |
| AhnRghLh.sys | 325980 | Ahnlab |
| AszFltNt.sys | 325970 | Ahnlab |
| OMFltLh.sys | 325960 | Ahnlab |
| V3Flu2k.sys | 325950 | Ahnlab |
| TfFregNt.sys | 325940 | AhnLab Inc. |
| AdcVcsNT.sys | 325930 | Ahnlab |
| vcdriv.sys | 325820 | Greatsoft Corp.Ltd |
| vcreg.sys | 325810 | Greatsoft Corp.Ltd |
| vchle.sys | 325800 | Greatsoft Corp.Ltd |
| NxFsMon.sys | 325700 | Novatix Corporation |
| LiveGuardAntiCheat.sys | 325650 | LiveGuard Software Ltd. |
| AntiLeakFilter.sys | 325600 | Individual developer (Soft3304) |
| NanoAVMF.sys | 325510 | Panda Software |
| shldflt.sys | 325500 | Panda Software |
| nprosec.sys | 325410 | Norman ASA |
| nregsec.sys | 325400 | Norman ASA |
| issregistry.sys | 325300 | IBM |
| THFilter.sys | 325200 | Sybonic Systems Inc |
| pervac.sys | 325100 | PerSystems SA |
| avgmfx86.sys | 325000 | AVG Grisoft |
| avgmfx64.sys | 325000 | AVG Grisoft |
| avgmfi64.sys | 325000 | AVG Grisoft |
| avgmfrs.sys (retired) | 325000 | AVG Grisoft |
| FortiAptFilter.sys | 324930 | Fortinet Inc. |
| fortimon2.sys | 324920 | Fortinet Inc. |
| fortirmon.sys | 324910 | Fortinet Inc. |
| fortishield.sys | 324900 | Fortinet Inc. |
| mscan-rt.sys | 324800 | SecureBrain Corporation |
| sysdiag.sys | 324600 | Huorong Security |
| agentrtm64.sys | 324510 | WINS CO. LTD |
| rswmon.sys | 324500 | WINS CO. LTD |
| mwfsmfltr.sys | 324420 | MicroWorld Software Services Pvt. Ltd. |
| gtkdrv.sys | 324410 | GridinSoft LLC |
| GbpKm.sys | 324400 | GAS Tecnologia |
| crnsysm.sys | 324310 | Coranti Inc. |
| crncache32.sys | 324300 | Coranti Inc. |
| crncache64.sys | 324300 | Coranti Inc. |
| egambit.sys | 324242 | TEHTRI-Security |
| drwebfwft.sys | 324210 | Doctor Web |
| DwShield.sys | 324200 | Doctor Web |
| DwShield64.sys | 324200 | Doctor Web |
| IProtect.sys | 324150 | EveryZone Inc. |
| TvFiltr.sys | 324140 | EveryZone INC. |
| TvDriver.sys | 324130 | EveryZone INC. |
| TvSPFltr.sys | 324120 | EveryZone INC. |
| TvPtFile.sys | 324110 | EveryZone INC. |
| TvStFltr.sys | 324101 | EveryZone INC. |
| TvMFltr.sys | 324100 | Everyzone |
| SophosED.sys | 324050 | Sophos |
| SAVOnAccess.sys | 324010 | Sophos |
| savonaccess.sys | 324000 | Sophos |
| sld.sys | 323990 | Sophos |
| OADevice.sys | 323900 | Tall Emu |
| pwipf6.sys | 323800 | PWI, Inc. |
| EstRkmon.sys | 323700 | ESTsoft corp. |
| EstRkr.sys - 64bit | 323700 | ESTsoft corp. |
| dwprot.sys | 323610 | Doctor Web |
| Spiderg3.sys | 323600 | Doctor Web Ltd. |
| STKrnl64.sys | 323500 | Verdasys Inc |
| UFDFilter.sys | 323400 | Yoggie |
| SCFltr.sys | 323300 | SecurityCoverage, Inc. |
| fildds.sys | 323200 | Filseclab |
| fsfilter.sys | 323100 | MastedCode Ltd |
| fpav_rtp.sys | 323000 | f-protect |
| cwdriver.sys | 322900 | Leith Bade |
| AYFilter.sys | 322810 | ESTsoft |
| Rtw.sys | 322800 | ESTsoft |
| EscFilter.sys | 322790.5 | ESTsecurity Corp |
| RSRtw.sys | 322790 | ESTsecurity Corp |
| RSPCRtw.sys | 322780 | ESTsecurity Corp |
| HookSys.sys | 322700 | Beijing Rising Information Technology Corporation Limited |
| snscore.sys | 322600 | S.N.Safe&Software |
| ssvhook.sys | 322500 | SecuLution GmbH |
| strapvista.sys | 322400 | AvSoft Technologies |
| strapvista64.sys | 322400 | AvSoft Technologies |
| sascan.sys | 322300 | SecureAge Technology |
| savant.sys | 322200 | Savant Protection, Inc. |
| VrARnFlt.sys | 322161 | HAURI |
| VrBBDFlt.sys | 322160 | HAURI |
| vrSDfmx.sys | 322153 | HAURI |
| vrSDfmx.sys | 322152 | HAURI |
| vrSDam.sys | 322151 | HAURI |
| vrSDam.sys | 322150 | HAURI |
| VRAPTFLT.sys | 322140 | HAURI Inc. |
| VrAptDef.sys | 322130 | HAURI |
| VrSdCore.sys | 322120 | HAURI |
| VrFsFtM.sys | 322110 | HAURI |
| VrFsFtMX.sys(AMD64) | 322110 | HAURI |
| vradfil2.sys | 322100 | HAURI |
| zgflt.sys | 322050 | ZeroGuard Ltd |
| fsgk.sys | 322000 | f-secure |
| bouncer.sys | 321950 | CoreTrace Corporation |
| PCTCore64.sys | 321910 | PC Tools Pty. Ltd. |
| PCTCore.sys (Old name) | 321910 | PC Tools Pty. Ltd. |
| ikfilesec.sys | 321900 | PC Tools Pty. Ltd. |
| ZxFsFilt.sys | 321800 | Australian Projects |
| antispyfilter.sys | 321700 | C-NetMedia Inc |
| dfndr_am.sys | 321654 | PSafe Ltd. |
| hlprotect.sys | 321650 | HarfangLab |
| PZDrvXP.sys | 321600 | VisionPower Co., Ltd. |
| haggc.sys | 321510.1 | Quick Heal Technologies Pvt. Ltd. |
| ggc.sys | 321510 | Quick Heal TechnologiesPvt. Ltd. |
| catflt.sys | 321500 | Quick Heal TechnologiesPvt. Ltd. |
| shhflt.sys |  | Quick Heal Technologies Pvt. Ltd. |
| snsrflt.sys(retired) | 321495 | Quick Heal Technologies Pvt. Ltd. |
| ztflt.sys | 321490.1 | Quick Heal Technologies Pvt. Ltd |
| bdsflt.sys | 321490 | Quick Heal Technologies Pvt. Ltd. |
| dartflt.sys | 321485 | Quick Heal Technologies Pvt. Ltd. |
| arwflt.sys | 321480 | Quick Heal Technologies Pvt. Ltd. |
| csagent.sys | 321410 | CrowdStrike Ltd. |
| kmkuflt.sys | 321400 | Komoku Inc. |
| ntguard.sys | 321337 | IKARUS Security |
| epdrv.sys | 321320 | McAfee Inc. |
| mfencoas.sys | 321310 | McAfee Inc. |
| mfehidk.sys | 321300 | McAfee Inc. |
| swin.sys | 321250 | McAfee Inc. |
| CyvrFsfd.sys | 321234 | Palo Alto Networks |
| cmdccav.sys | 321210 | Comodo Group Inc. |
| cmdguard.sys | 321200 | Comodo Group Inc. |
| mfesec.sys | 321150.5 | McAfee, LLC |
| cbfilter20.sys | 321120.5 | CMC Cyber Security |
| cbprocess20.sys | 321120 | CMC Cyber Security |
| cbregistry20.sys | 321120 | CMC Cyber Security |
| nycu_filter.sys | 321110.5 | NYCU |
| K7Sentry.sys | 321100 | K7 Computing Private Ltd. |
| nsminflt.sys | 321050 | NHN |
| nsminflt64.sys | 321050 | NHN |
| nvcmflt.sys | 321000 | Norman |
| dgsafe.sys | 320950 | KINGSOFT |
| issfltr.sys | 320900 | ISS |
| hbflt.sys | 320840 | BitDefender SRL |
| vlflt.sys | 320832 | BitDefender SRL |
| bdsvm.sys | 320830 | Bitdefender |
| gzflt.sys | 320820 | BitDefender SRL |
| bddevflt.sys | 320812 | BitDefender SRL |
| ignis.sys | 320811 | BitDefender SRL |
| AVCKF.SYS | 320810 | BitDefender SRL |
| bdfsfltr.sys | 320800 | Softwin |
| bdfm.sys | 320790 | Softwin |
| gemma.sys | 320782 | BitDefender SRL |
| Atc.sys | 320781 | BitDefender SRL |
| AVC3.SYS | 320780 | BitDefender SRL |
| TRUFOS.SYS | 320770 | BitDefender SRL |
| aswmonflt.sys | 320700 | Alwil |
| kavnsi.sys | 320650 | AVNOS |
| TaegisKM.x64.sys | 320640.5 | Secureworks Inc. |
| TaegisKM.x86.sys | 320640.5 | Secureworks Inc. |
| CiscoSAM.sys | 320618 | Cisco Systems |
| immunetselfprotect.sys | 320616 | Cisco Systems |
| immunetprotect.sys | 320614 | Cisco Systems |
| CiscoAMPCEFWDriver.sys | 320612 | Cisco Systems |
| CiscoAMPHeurDriver.sys | 320610 | Cisco Systems |
| HookCentre.sys | 320602 | G Data |
| PktIcpt.sys | 320601 | G Data |
| MiniIcpt.sys | 320600 | G Data |
| acdrv.sys | 320520 | OnMoon Company LLC |
| tmfsdrv2.sys | 320510 | Teramind |
| avgntflt.sys | 320500 | Avira GmbH |
| klam.sys | 320450 | Kaspersky Lab |
| klbg.sys | 320440 | Kaspersky |
| kldback.sys | 320430 | Kaspersky |
| kldlinf.sys | 320420 | Kaspersky |
| kldtool.sys | 320410 | Kaspersky |
| klif.sys | 320401 | Kaspersky Lab |
| klif.sys | 320400 | Kaspersky |
| klam.sys | 320350 | Kaspersky Lab |
| hsmltwhl.sys | 320340 | Hitachi Solutions |
| hssfwhl.sys | 320330 | Hitachi Solutions |
| DeepInsFS.sys | 320323 | Deep Instinct Ltd. |
| DeepInsFS.sys | 320322 | Deep Instinct Ltd. |
| DeepInsFS.sys | 320321 | Deep Instinct Ltd. |
| DeepInsFS.sys | 320320 | Deep Instinct Ltd. |
| avfsmn.sys | 320310 | Anvisoft |
| lbd.sys | 320300 | Lavasoft AB |
| oavnflt.sys | 320250 | OpenAVN Inc |
| pavdrv.sys | 320210 | Panzor Cybersecurity |
| rvsmon.sys | 320200 | CJSC Returnil Software |
| KawachFsMinifilter.sys | 320160 | Sequretek IT |
| securoFSD_x64.sys | 320150 | knowwheresoft Ltd |
| securoFS.sys | 320149 | knowwheresoft Ltd |
| WRAEKernel.sys | 320112 | Webroot Inc. |
| WRKrn.sys | 320111 | Webroot Inc. |
| WRCore.x64.sys | 320110.99 | Webroot Inc. |
| WRCore.x86.sys | 320110.99 | Webroot Inc. |
| ARCore.x64.sys | 320110.98 | Webroot Inc. |
| ARCore.x86.sys | 320110.98 | Webroot Inc. |
| WRCore.sys | 320110 | Webroot Inc. |
| ssfmonm.sys | 320100 | Webroot Software, Inc. |
| euimgprt.sys | 320085.5 | EaseUS |
| ODFsFimFilter.sys | 320070 | Odyssey Cyber Security |
| ODFsTokenFilter.sys | 320061 | Odyssey Cyber Security |
| ODFsFilter.sys | 320060 | Odyssey Cyber Security |
| vk_fsf.sys | 320050 | AxBx |
| VirtualAgent.sys | 320005 | Symantec |

## 300000 - 309998: FSFilter Replication

| Minifilter                  | Altitude | Company                                 |
|-----------------------------|----------|-----------------------------------------|
| IntelCAS.sys | 309100 | Intel Corporation |
| mvfs.sys | 309000 | IBM Corporation |
| ExtVol.sys | 307900.5 | I-O DATA DEVICE, INC. |
| frxccd.sys | 306000 | FSLogix Inc. |
| dvfilter.sys | 305002 | Microsoft |
| fsrecord.sys | 305000 | Microsoft |
| esff.sys | 304500 | Beijing Cloudock Techn Co |
| InstMon.sys | 304201 | Numecent Inc. |
| StreamingFSD.sys | 304200 | Numecent Inc. |
| ubcminifilterdriver.sys | 304100 | Ullmore Ltd. |
| replistor.sys | 304000 | Legato |
| stfsd.sys | 303900 | Endeavors Technologies |
| xomf.sys | 303800 | CA (XOSOFT) |
| nfid.sys | 303700 | Neverfail Group Ltd |
| sybfilter.sys | 303600 | Sybase, Inc. |
| rfsfilter.sys | 303500 | Evidian |
| cvmfsj.sys | 303400 | CommVault Systems, Inc. |
| iOraFilter.sys | 303300 | Infonic plc |
| bkbmfd32.sys (x86) | 303200 | BakBone Software, Inc |
| bkbmfd64.sys (x64) | 303200 | BakBone Software, Inc |
| mblvn.sys | 303100 | Packeteer |
| AV12NFNT.sys | 303000 | AhnLab |
| mDP_win_mini.sys | 302900 | Macro Impact |
| ctxubs.sys | 302800 | Citrix Systems Inc. |
| rrepfsf.sys | 302700 | Rose Datasystems Inc |
| zrbd.sys | 302110.3 | Shanghai Fangye Network |
| zrbdlock.sys | 302110.2 | Shanghai Fangye Network |
| wsyncd.sys | 302100 | WANFast LLC |
| cbfsfilter2017.sys | 301900 | Super Flexible Software |
| AxFilter.sys | 301800 | Axcient Inc. |
| vxfsrep.sys | 301700 | Symantec |
| dellcapfd.sys | 301600 | Dell Inc. |
| Sptres.sys | 301500 | Safend |
| OfficeBackup.sys | 301400 | Ushus Technologies |
| LxFileMirror.sys | 301350 | Techit GmbH |
| pcvnfilt.sys | 301300 | Blue Coat |
| repdac.sys | 301200 | NSI |
| repkap.sys | 301100 | NSI |
| repdrv.sys | 301000 | NSI |

## 280000 - 289998: FSFilter Continuous Backup

| Minifilter                  | Altitude | Company                                 |
|-----------------------------|----------|-----------------------------------------|
| SyncODFA.sys | 289010 | Sync.com Inc |
| File_monitor.sys | 289000 | Acronis |
| Klcdp.sys | 288900 | Kaspersky Lab |
| splitinfmon.sys | 288800 | Split Infinity |
| versamatic.sys | 288700 | Acertant Tech |
| Yfilemon.sys | 288690 | Yarisoft |
| ibac.sys | 288600 | Idealstor, LLC. |
| fkdriver.sys | 288500 | Filekeeper |
| AAFileFilter.sys | 288300 | Dell Inc. |
| cbfilter20.sys | 288290.5 | Mobile Content mgmt |
| hyperoo.sys | 288400 | Hyperoo Ltd |
| EioHelium.sys | 287777.5 | Elastio Software Inc |
| HyperBacCA.sys | 285000 | Red Gate Software Ltd |
| ZMSFsFltr.sys | 284400 | Zenith InfoTech |
| AlfaSC.sys | 284300 | Alfa Corporation |
| hie_ifs.sys | 284200 | Hie Electronics, Inc. |
| cbfilter20.sys | 284150.5 | Datto Inc |
| AAFs.sys | 284100 | AppAssure Software |
| defilter.sys (old) | 284000 | Microsoft |
| aFsvDrv.sys | 283100 | ITSTATION Inc |
| tilana.sys | 283000 | Tilana Sys |
| VmDPFilter.sys | 282900 | Macro Impact |
| LbFilter.sys | 281700 | Linkverse S.r.l. |
| fbsfd.sys | 281600 | Ferro Software |
| dupleemf.sys | 281500 | Duplee SPI, S.L. |
| file_tracker.sys | 281420 | Acronis Inc. |
| exbackup.sys | 281410 | Acronis Inc. |
| afcdp.sys | 281400 | Acronis Inc. |
| dcefltr.sys | 281300 | Cofio Software Ltd |
| ipmrsync_mfilter.sys | 281200 | OpenMars Enterprises |
| cascade.sys | 281100 | JP Software |
| filearchive.sys | 281000 | Code Mortem |
| syscdp.sys | 280900 | System OK AB |
| dpnedriver.sys   (x86) | 280850 | HP |
| dpnedriver64.sys (x64) | 280850 | HP |
| hpchgflt.sys | 280800 | HP |
| VirtFile.sys | 280700 | Veritas |
| DeqoCPS.sys | 280600 | Deqo |
| LV_Tracker.sys | 280500 | LiveVault |
| cpbak.sys | 280410 | Checkpoint Software |
| tdmonxp.sys | 280400 | TimeData |
| nvfr_cpd | 280310 | Bakbone Software Inc. |
| nvfr_fdd | 280300 | Bakbone Software Inc. |
| Sptbkp.sys | 280290 | Safend |
| accessmonitor.sys | 280280 | Briljant Ekonomisystem |

## 260000 - 269998: FSFilter Content Screener

| Minifilter                  | Altitude | Company                                 |
|-----------------------------|----------|-----------------------------------------|
| QDocumentDPI.sys | 268600.5 | Bicdroid Inc |
| anrfsdrv.sys | 268500 | ANR Co. LTD. |
| wzProcCut.sys | 268350.875 | ITSTATION Inc. |
| taResource.sys | 268350.75 | ITSTATION Inc. |
| wzPrtProc.sys | 268350.5 | ITSTATION Inc. |
| taExeScanner.sys | 268350 | ITSTATION Inc. |
| GuardFSFlt.sys | 268340 | ProShield |
| usbguard.sys | 268330 | HangZhou Tease Tech |
| gibepdevflt.sys | 268320 | Group-IB LTD |
| EffeDriver.sys | 268310 | DROVA |
| Klshadow.sys | 268300 | Kaspersky Lab |
| TN28.sys | 268290 | ID Authentication Tech |
| PGDriver.sys | 268280 | Avecto Ltd |
| itseczvdb.sys | 268270 | Innotium Inc |
| unimon.sys | 268265.5 | Unify Technologies |
| isarsd.sys | 268260 | ISARS |
| zeoscanner.sys | 268255 | PCKeeper |
| fileHiders.sys | 268250 | PCKeeper |
| cbfltfs4-ObserveIT.sys | 268240 | ObserveIT |
| hipara.sys | 268230 | Allsum LLC |
| AliFileMonitorDriver.sys | 268220 | Alibaba |
| writeGuard.sys | 268210 | TCXA Ltd. |
| KKUDKProtectKer.sys | 268200 | Goldmessage technology co., Ltd. |
| HAWKFIMInt.sys | 268190 | HAWK Network Defense |
| esaccctl.sys | 268180 | EgoSecure GmbH |
| WSguard.sys | 268170 | Wiper Software UAB |
| Atomizer.sys | 268160 | DragonFlyCodeWorks |
| farwflt.sys | 268150 | Malwarebytes |
| ADSpiderEx2.sys | 268140 | Digitalonnet |
| sdfilter.sys | 268130 | Igor Zorkov |
| Safe.sys | 268120 |  |
| mydlpdelete-scanner.sys | 268110 | Medra Teknoloji |
| mydlpscanner.sys | 268100 | Medra Teknoloji |
| VrMacFlt.sys | 268080 | Hauri Inc |
| hnpro.sys | 268040 | Solupia |
| DLDriverNetMini.sys | 268030 | DeviceLock Inc |
| ENFFLTDRV.sys | 268020 | Enforcive Systems |
| imagentpg.sys | 268012 | Infomaximum |
| crocopg.sys | 268010 | Infomaximum |
| sbapifs.sys | 268000 | Sunbelt Software |
| H6kernNT.sys | 267920 | H6N Technologies LLC |
| SGKD32.SYS | 267910 | NetSection Security |
| IccFilter.sys | 267900 | NEC System Technologies |
| tflbc.sys | 267800 | Tani Electronics Corporation |
| ArmFlt.sys | 267000 | Armor Antivirus |
| WBDrv.sys | 266700 | Axiana LLC |
| DMSamFilter.sys | 266600 | Digimarc Corp. |
| mumbl.sys | 266540 | ZenmuTech Inc. |
| DLPDriverSmb.sys | 266400.5 | Acronis |
| spiderfilter.sys | 266250.5 | Guangzhou Shizhen Information Technology Co.,Ltd |
| 5nine.cbt.sys | 266100 | 5nine Software Inc. |
| bsfs.sys | 266000 | Quick Heal TechnologiesPvt. Ltd.  |
| XXRegSFilter.sys | 265910 | Zhe Jiang Xinxin Software Tech. |
| XXSFilter.sys | 265900 | Zhe Jiang Xinxin Software Tech. |
| AloahaUSBBlocker.sys | 265800 | Wrocklage Intermedia |
| frxdrv.sys | 265700 | FSLogix Inc. |
| upmAction.sys | 265650.5 | Citrix Systems |
| FolderSecure.sys | 265600 | Max Secure Software |
| XendowFLTC.sys | 265570 | Credant Technologies |
| RepDac | 265500 | Vision Solutions |
| tbbdriver.sys | 265400 | Tedesi |
| spcgrd.sys | 265300 | FUJITSU BROAD SOLUTION |
| fdtlock.sys | 265250 | FUJITSU BROAD SOLUTION & CONSULTING Inc. |
| ssfFSC.sys | 265200 | SECUWARE S.L. |
| GagSecurity.sys | 265120 | Beijing Shu Yan Science |
| PrintDriver.sys | 265110 | Beijing Shu Yan Science |
| activ.sys | 265100 | Rapidware Pty Ltd |
| avscan.sys | 265010 | Microsoft |
| scanner.sys | 265000 | Microsoft |
| DI_fs.sys | 264910 | Soft-SB |
| wgnpos.sys | 264900 | Orchestria |
| odfltr.sys | 264810 | NetClean Technologies |
| ncpafltr.sys | 264800 | NetClean Technologies |
| ct.sys | 264700 | Haute Secure |
| fvefsmf.sys | 264600 | Fortisphere, Inc. |
| block.sys | 264500 | Autonomy Systems Limited |
| csascr.sys | 264400 | Cisco Systems |
| SymAFR.sys | 264300 | Symantec Corporation |
| cwnep.sys | 264200 | Websense Inc. |
| spywareremover.sys | 264150 | C-Netmedia |
| malwarebot.sys | 264140 | C-Netmedia |
| antispywarebot.sys | 264130 | 2Squared Inc. |
| adwarebot.sys | 264120 | AntiSpyware LLC |
| antispyware.sys | 264110 | AntiSpyware LLC |
| spywarebot.sys | 264100 | C-Netmedia |
| nomp3.sys | 264000 | Hamish Speirs (private developer) |
| dlfilter.sys | 263900 | Starfield Software |
| sifsp.sys | 263800 | Secure Islands Technologies LTD |
| DLFsFlt.sys | 263700 | CenterTools Software GmbH |
| SamKeng.sys | 263600 | Syvik Co, Ltd. |
| rml.sys | 263500 | Logis IT Service Gmbh |
| vfsmfd.sys | 263410 | Vontu Inc. |
| vfsmfd.sys | 263400 | Vontu Inc. |
| acfilter.sys | 263300 | Avalere, Inc. |
| psecfilter.sys | 263200 | MDI Laboratory, Inc. |
| SolRedirect.sys | 263110 | Soliton Systems |
| solitkm.sys | 263100 | Soliton Systems |
| ipcfs.sys | 263000 | NetVeda |
| netgateav_access.sys | 262910 | NETGATE Tech. s.r.o. |
| spyemrg_access.sys | 262900 | NETGATE Tech. s.r.o. |
| pxrmcet.sys | 262800 | Proxure Inc. |
| EgisTecFF.sys | 262700 | Egis Technology Inc. |
| fgcpac.sys | 262600 | Fortres Grand Corp. |
| saappctl.sys | 262510 | SecureAge Technology |
| sadlp.sys | 262500 | SecureAge Technology |
| MtUsbBlockerFlt.sys | 261420.5 | Matisoft Cyber Security |
| CRExecPrev.sys | 262410 | Cybereason |
| PEG2.sys | 262400 | PE GUARD |
| AdminRunFlt.sys | 262300 | Simon Jarvis |
| wvscr.sys | 262200 | Chengdu Wei Tech Inc. |
| psepfilter.sys | 262100 | Absolute Software |
| SAMDriver.sys | 262000 | Summit IT |
| emrcore.sys | 261920 | Ivanti Inc |
| wire_fsfilter.sys | 261910 | ThreatSpike Labs |
| AMFileSystemFilter.sys | 261900 | AppSense Ltd |
| mtflt.sys | 261880 | mTalos Inc. |
| nxrmflt.sys | 261680 | NextLabs, Inc. |
| RsFltScanner.sys | 261400.5 | SecuritySnares |
| oc_fsfilter.sys | 261300 | Raiffeisen Bank Aval |
| IslandDrv.sys | 261250.5 | Island Technology Inc. |
| hdlpflt.sys | 261200 | McAfee Inc. |
| CCFFilter.sys | 261160 | Microsoft |
| cbafilt.sys | 261150 | Microsoft |
| SmbBandwidthLimitFilter.sys | 261110 | Microsoft |
| DfsrRo.sys | 261100 | Microsoft |
| DataScrn.sys | 261000 | Microsoft |
| ldusbro.sys | 260900 | LANDesk Inc. |
| FileScreenFilter.sys | 260800 | Veritas |
| cpAcOnPnP.sys | 260720 | conpal GmbH |
| cpsgfsmf.sys | 260710 | conpal GmbH |
| psmmfilter.sys | 260700 | PolyServe |
| pctefa.sys | 260650 | PC Tools Pty. Ltd. |
| pctefa64.sys | 260650 | PC Tools Pty. Ltd. |
| SymEFASI64.sys | 260620 | NortonLifeLock Inc. |
| SymEFASI.sys | 260620 | NortonLifeLock Inc. |
| symefasi.sys | 260610 | Symantec Corporation |
| symefa.sys | 260600 | Symantec |
| symefa64.sys | 260600 | Symantec |
| apdFSF.sys | 260550 | Cyberbit Ltd |
| aictracedrv_cs.sys | 260500 | AI Consulting |
| DWFIxxxx.sys | 260410 | SciencePark Corporation |
| DWFIxxxx.sys | 260400 | SciencePark Corporation |
| ElasticEndpoint.sys | 260350.5 | Elastic |
| dlpflt.sys | 260340 | Digital Endpoint |
| DSDriver.sys | 260330 | ManageEngine Zoho Corp |
| mcfltlab.sys | 260320 | Beijing MicroColor |
| FDriver.sys | 260310 | Fox-IT |
| iqpk.sys | 260300 | Secure Islands Technologies LTD |
| ZTkrnlOpRg.sys | 260264 | Trustsoft |
| ZTkrnlNt.sys | 260262 | Trustsoft |
| ZTkrnl.sys | 260260 | Trustsoft |
| VHDFlt.sys | 260240 | Dell |
| VHDFlt.sys | 260230 | Dell |
| VHDFlt.sys | 260220 | Dell |
| VHDFlt.sys | 260210 | Dell |

## 240000 - 249999: FSFilter Quota Management

| Minifilter                  | Altitude | Company                                 |
|-----------------------------|----------|-----------------------------------------|
| dfx-qfs-fltr.sys | 245100 | DefendX Software |
| ntps_qfs.sys | 245100 | DefendX Software |
| PSSFsFilter.sys | 245000 | PSS Systems |
| Sptqmg.sys | 245300 | Safend |
| storqosflt.sys | 244000 | Microsoft |

## 220000 - 229999: FSFilter System Recovery

| Minifilter                  | Altitude | Company                                 |
|-----------------------------|----------|-----------------------------------------|
| file_protector.sys | 227000 | Acronis |
| fbwf.sys | 226000 | Microsoft |
| Ranger.sys | 221800.5 | ByteJams B.V. |
| BoldendDrvr.sys | 221700.5 | Boldend, Inc. |
| hmpalert.sys | 221600 | SurfRight |
| Klsysrec.sys | 221500 | Kaspersky Lab |
| SFDRV.SYS | 221400 | Utixo LLC |
| sp_prot.sys | 221300 | Xacti Corporation |
| nsfilep.sys | 221200 | Netsupport Limited |
| syscow.sys | 221100 | System OK AB |
| fsredir.sys | 221000 | Microsoft |

## 200000 - 209999: FSFilter Cluster File System

| Minifilter                  | Altitude | Company                                 |
|-----------------------------|----------|-----------------------------------------|
| CVCBT.sys | 203400 | CommVault Systems, Inc. |
| ResumeKeyFilter.sys | 202000 | Microsoft |
| VeeamFCT.sys | 201900 | Veeam Software |
| ShadowVirtualStorage.sys | 201800 | Blade SAS |

## 180000 - 189999: FSFilter HSM

| Minifilter                  | Altitude | Company                                 |
|-----------------------------|----------|-----------------------------------------|
| wcifs.sys | 189900 | Microsoft |
| prjflt.sys | 189800 | Microsoft |
| p4vfsflt.sys | 189700.5 | Microsoft |
| gameflt.sys | 189750 | Microsoft |
| nvmsqrd.sys | 188900 | NVIDIA Corporation |
| Ghost_file.sys | 188800 | Acronis |
| PeerTier.sys | 187900.5 | Peer Software Inc. |
| RsFlt.sys | 187000 | Redstor Limited |
| CloudTier.sys | 186900.5 | EaseFilter Technologies |
| mnefs.sys | 186800 | Nippon Techno Lab |
| Svfsf.sys | 186700 | Spharsoft Technologies |
| uVaultFlt.sys | 186650 | DOR |
| syncmf.sys | 186620 | Oxygen Cloud |
| gwmemory.sys | 186600 | Macrotec LLC |
| cteraflt.sys | 186550 | CTERA Networks Ltd. |
| dbx.sys | 186500 | Dropbox Inc. |
| iMDrvFlt.sys | 186450 | iManage LLC |
| quaddrasi.sys | 186400 | Quaddra Software |
| gdrive.sys | 186300 | Google |
| CoreSyncFilter.sys | 186250 | Adobe Systems Inc. |
| EaseTag.sys | 186200 | EaseVault Technologies Inc. |
| HSFilter.sys | 186150 | HubStor Inc. |
| hcminifilter.sys | 186100 | Happy Cloud Inc. |
| PDFsFilter.sys | 186000 | Raxco Sfotware Inc. |
| camino.sys | 185900 | CaminoSoft Corp |
| C2C_AF1R.SYS | 185810 | C2C Systems |
| DFdriver.sys | 185800 | DataFirst Corporation |
| amfadrv.sys | 185700 | Quest Software Inc. |
| HSMdriver.sys | 185600 | Wim Vervoorn |
| kdfilter.sys | 185555 | Komprise Inc. |
| htdafd.sys | 185500 | Bridgehead Soft |
| odphflt.sys | 180455 | Microsoft |
| cldflt.sys | 180451 | Microsoft |
| SymHsm.sys | 185400 | Symantec |
| evmf.sys | 185100 | Symantec |
| otfilter.sys | 185000 | Overtone Soft |
| ithsmdrv.sys | 184900 | IBM |
| MfaFilter.sys | 184800 | Waterford Technologies |
| SonyHsmMinifilter.sys | 184700 | Sony Corporation |
| acahsm.sys | 184600 | Autonomy Corporation |
| zlhsm.sys | 184500 | ZL Technologies |
| CFileProtect.sys | 184100 | Zhejiang Security Tech |
| stc_restore_filter.sys | 184000 | StorageCraft Technology |
| dvfilter.sys | 183003 | Microsoft |
| Accesstracker.sys | 183002 | Microsoft |
| Changetracker.sys | 183001 | Microsoft |
| Fstier.sys | 183000 | Microsoft |
| hsmcdpflt.sys | 182700 | Metalogix |
| archivmgr.sys | 182690 | Metalogix |
| ntps_oddm.sys | 182600 | DefendX Software |
| XDFileSys.sys | 182500 | XenData Limited |
| upmjit.sys | 182400 | Citrix Systems |
| AtmosFS.sys | 182310 | EMC Corporation |
| DxSpy.sys | 182300 | EMC Software Inc. |
| car_hsmflt.sys | 182200 | Caringo, Inc. |
| BRDriver.sys | 182100 | BitRaider |
| BRDriver64.sys | 182100 | BitRaider |
| autnhsm.sys | 182000 | Autonomy Corporation |
| cthsmflt.sys | 181970 | ComTrade |
| NxMini.sys | 181900 | NEXSAN |
| neuflt.sys | 181818 | NeuShield |
| npfdaflt.sys | 181800 | Mimosa Systems Inc |
| AppStream.sys | 181700 | AppStream, Inc. |
| HPEDpHsmX64.sys | 181620 | Hewlett-Packard, Co. |
| HPArcHsmX64.sys | 181610 | Hewlett-Packard, Co. |
| hphsmflt.sys | 181600 | Hewlett-Packard, Co. |
| cparchsm.sys | 181610 | Micro Focus |
| RepHsm.sys | 181500 | Double-Take Software, Inc. |
| RepSIS.sys | 181490 | Double-Take Software |
| SquashCompressionFsFilter.sys | 181410 | Squash Compression |
| GXHSM.sys | 181400 | Commvault Systems, Inc |
| EdsiHsm.sys | 181300 | Enterprise Data Solutions, Inc. |
| BkfMap.sys | 181200 | Data Storage Group |
| hsmfilter.sys | 181100 | GRAU Data Storage AG |
| mwilcflt.sys | 181020 | Moonwalk Universal P/L |
| mwildflt.sys | 181015 | Moonwalk Universal P/L |
| mwilsflt.sys | 181010 | Moonwalk Universal P/L |
| mwidmflt.sys | 181000 | Moonwalk Universal P/L |
| HcpAwfs.sys | 181960 | Hitachi Data Systems |
| sdrefltr.sys | 180950 | Hitachi Data Systems |
| fltasm.sys | 180900 | Global 360 |
| cnet_hsm.sys | 180850 | Carroll-Net Inc. |
| pntvolflt.sys | 180800 | PoINT Software&Systems |
| appxstrm.sys | 180710 | Microsoft |
| wimmount.sys | 180700 | Microsoft |
| hsmflt.sys | 180600 | Microsoft |
| dfsrflt.sys | 180500 | Microsoft |
| StorageSyncGuard.sys | 180465 | Microsoft |
| StorageSync.sys | 180460 | Microsoft |
| dedup.sys | 180450 | Microsoft |
| dfmflt.sys | 180410 | Microsoft |
| sis.sys | 180400 | Microsoft |
| rbt_wfd.sys | 180300 | Riverbed Technology,Inc |

## 170000 - 174999: *FSFilter Imaging (ex: .ZIP)

| Minifilter                  | Altitude | Company                                 |
|-----------------------------|----------|-----------------------------------------|
| pfmfs_???.sys | 172100 | Pismo Technic Inc |
| virtual_file.sys | 172000 | Acronis |
| wimFltr.sys | 170500 | Microsoft |

## 160000 - 169999: FSFilter Compression

| Minifilter                  | Altitude | Company                                 |
|-----------------------------|----------|-----------------------------------------|
| CmgFFC.sys | 166000 | Credant Technologies |
| compress.sys | 165000 | Microsoft |
| cmpflt.sys | 162000 | Microsoft |
| IridiumIO.sys | 161700 | Confio |
| zzenc.sys | 161650.5 | Imdtech LLC |
| logcompressor.sys | 161600 | VelociSQL Inc. |
| GcfFilter.sys | 161500 | GemacmbH |
| ssddoubler.sys | 161400 | Sinan Karaca |
| Sptcmp.sys | 161300 | Safend |
| wimfsf.sys | 161000 | Microsoft |
| GEFCMP.sys | 160100 | Symantec |

## 140000 - 149999: FSFilter Encryption

| Minifilter                  | Altitude | Company                                 |
|-----------------------------|----------|-----------------------------------------|
| SCEfd.sys | 149500.5 | SOFTCAMP Co.LTD |
| AAFS.sys | 149110 | ViGero |
| FJSeparettiFilterRamMon.sys | 149100 | FUJITSU LIMITED |
| VSCCryptor.sys | 149065.5 | Guangzhou Junkai Electronic Technology Co |
| trsxefs.sys | 149060 | TransientX Inc. |
| psatfilter.sys | 149050 | ProYuga |
| RdFilter.sys | 149040 | CyberEye Research Labs |
| gisfile_decryption.sys | 149030 | Communication U China |
| TIFSFilter.sys | 149020 | SG Corporation |
| OsrDt2.sys | 149010 | Information Security Corp |
| EasyKryptMF.sys | 149000 | SoftKrypt LLC |
| padlock.sys | 148910 | IntSoft Inc. |
| ffecore.sys | 148900 | Winmagic |
| bkfs.sys | 148880 | Hangzhou JoyBlock Ltd |
| fangcloud.sys | 148860 | Hangzhou Yifangyun |
| FileGuard.sys | 148820.5 | EaseFilter Technologies |
| klvfs.sys | 148810 | Kaspersky Lab |
| Klfle.sys | 148800 | Kaspersky Lab |
| ISFP.sys | 148701 | ALPS SYSTEM INTEGRATIO |
| ISIRM.sys | 148700 | ALPS SYSTEM INTERGRATION CO., LTD |
| fhfs.sys | 148670.5 | SecureCircle |
| ASUSSecDrive.sys | 148650 | ASUS |
| ABFilterDriver.sys | 148640 | AlertBoot |
| QDocumentFSF.sys | 148630 | BicDroid Inc. |
| bfusbenc.sys | 148620 | bitFence Inc. |
| sztgbfsf.sys | 148610 | SaferZone Co. |
| mwIPSDFilter.sys | 148600 | Egis Technology Inc. |
| csccvdrv.sys | 148500 | Computer Sciences Corporation |
| aefs.sys | 148400 | Angelltech Corporation Xi'an |
| VTEFsFlt.sys | 148374 | EsComputer Corp |
| IWCSEFlt.sys | 148300 | InfoWatch |
| GDDmk.sys | 148250 | G Data Software AG |
| clcxcore.sys | 148210 | AFORE Solutions Inc. |
| OrisLPDrv.sys | 148200 | CGS Publishing Tech |
| nlemsys.sys | 148100 | NETLIB |
| prvflder.sys | 148000 | Microsoft |
| ssefs.sys | 147900 | SecuLution GmbH |
| SePSed.sys | 147800 | Humming Heads, Inc. |
| dlmfencx.sys | 147700 | Data Encryption Ltd |
| SkyDEnc.sys | 147620 | Sky Co Ltd |
| psgcrypt.sys | 147610 | Yokogawa R&L Corp |
| bbfsflt.sys | 147600 | Bloombase |
| qx10efs.sys | 147500 | Quixxant |
| MEfefs.sys | 147400 | Eruces Inc. |
| medlpflt.sys | 147310 | Check Point Software Technologies Ltd |
| dsfa.sys | 147308 | Check Point Software Technologies Ltd |
| Snicrpt.sys | 147300 | Systemneeds, Inc |
| iCrypt.sys | 147200 | I-O DATA DEVICE, INC. |
| xdrmflt.sys | 147100 | bluefinsystems |
| dyFsFilter.sys | 147000 | Scrypto Media |
| thinairwin.sys | 146960 | Thin Air Inc |
| UcaDataMgr.sys | 146950 | AppSense Ltd |
| zesocc.sys | 146900 | Novell |
| CegisDlpFsFilter.sys | 146868.5 | Cegis Cyber Inc |
| mfprom.sys | 146800 | McAfee Inc |
| MfeEEFF.sys | 146790 | McAfee Inc. |
| intefs.sys | 146700 | TianYu Software |
| ADTDEAgent.sys | 146680.5 | Shanghai Andang Technology |
| leofs.sys | 146600 | Leotech |
| autocryptater.sys | 146500 | Richard Hagen |
| WavxDMgr.sys | 146400 | Scott Cochrane |
| eedmkxp32.sys | 146300 | Entrust |
| SbCe.sys | 146200 | SafeBoot |
| iSharedFsFilter | 146100 | Packeteer Inc |
| AHSentry.sys | 146050.5 | AutnHive Inc. |
| dlrmenc.sys | 146010 | DESlock |
| dlmfenc.sys | 146000 | DESlock |
| aksdf.sys | 145900 | Aladdin Knowledge Systems |
| DDSFilter.sys | 145800 | WuHan Forworld Software |
| SecureShield.sys | 145700 | HMI |
| AifaFE.sys | 145600 | Alfa |
| HiCrypt.sys | 145566 | digitronic computersysteme GmbH |
| GBFsMf.sys | 145500 | GreenBorder |
| jmefs.sys | 145400 | ShangHai Elec |
| emugufs.sys | 145333 | Emugu Secure FS |
| VFDriver.sys | 145300 | R Systems |
| IntelDG.sys | 145250 | Intel Corporation |
| DPMEncrypt.sys | 145240 | Randtronics Pty |
| EVSDecrypt64.sys | 145230 | Fortium Technologies Ltd |
| skycryptorencfs.sys | 145220 | Onecryptor CJSC. |
| AisLeg.sys | 145210 | Assured Information Security |
| windtalk.sys | 145200 | Hyland Software |
| TeamCryptor.sys | 145190 | iTwin Pte. Ltd. |
| CVDLP.sys | 145180 | CommVault Systems, Inc. |
| 5nine.encryptor.sys | 145170 | 5nine Software Inc. |
| ctpfile.sys | 145160 | Beijing Wondersoft Technology Co., Ltd |
| DPDrv.sys | 145150 | IBM Japan, Ltd. |
| tsdlp.sys | 145140 | Forware |
| KCDriver.sys | 145130 | Tallegra Ltd |
| CmgFFE.sys | 145120 | Credant Technologies |
| fgcenc.sys | 145110 | Fortres Grand Corp. |
| sview.sys | 145100 | Cinea |
| TalkeyFilterDriver.sys | 145040 | myTALKEY s.r.o. |
| MtUsbFlt19.sys | 145020.5 | Matisoft Cyber Security |
| FedsFilterDriver.sys | 145010 | Physical Optics Corp |
| stocc.sys | 145000 | Senforce Technologies |
| SnEfs.sys | 144900 | Informzaschita |
| ewSecureDox | 144800 | Echoworx Corporation |
| osrdmk.sys | 144700 | OSR Open Systems Resources, Inc. |
| uldcr.sys | 144600 | NCR Financial Solutions |
| Tkefsxp.sys - 32bit | 144500 | INCA Internet Co., Ltd |
| Tkefsxp64.sys - 64bit | 144500 | INCA Internet Co., Ltd |
| NmlAccf.sys | 144400 | NEC System Technologies, Ltd. |
| SolCrypt.sys | 144300 | Soliton Systems K.K. |
| IngDmk.sys | 144200 | Ingrian Networks, Inc. |
| llenc.sys | 144100 | SecureAxis Software |
| SecureData.sys | 144030 | SecureAge Technology |
| lockcube.sys | 144020 | SecureAge Technology Pte Ltd |
| sdmedia.sys | 144010 | SecureAge Technology |
| mysdrive.sys | 144000 | SecureAge Technology |
| FileArmor.sys | 143900 | Mobile Armor |
| VSTXEncr.sys | 143800 | VIA Technologies, Inc. |
| dgdmk.sys | 143700 | Verdasys Inc. |
| shandy.sys | 143600 | Safend Ltd. |
| C2knet.sys | 143520 | Secuware |
| C2kdef.sys | 143510 | Secuware |
| ssfFS.sys | 143500 | SECUWARE S.L. |
| PISRFE.sys | 143400 | Jilin University IT Co. |
| bapfecre.sys | 143300 | BitArmor Systems, Inc |
| KPSD.sys | 143200 | cihosoft |
| Fcfileio.sys | 143100 | Brainzsquare, Co. Ltd. |
| MonsterDrive.FsFilter.sys | 143050.5 | itMonster Ltd. |
| cpdrm.sys | 143000 | Pikewerks |
| vmsecfiltr.sys | 142900.5 | Thales CPL(previously Vormetric Inc) |
| vmfiltr.sys | 142900 | Vormetric Inc |
| Sfntpffd.sys | 142890 | Thales CPL |
| VFSEnc.sys | 142811 | Symantec |
| pgpfs.sys | 142810 | Symantec |
| fencry.sys | 142800 | Symantec |
| TmFileEncDmk.sys | 142700 | Trend Micro Inc |
| cpefs.sys | 142600 | Crypto-Pro |
| dekfs.sys | 142500 | KasherLab co.,ltd |
| qlockfilter.sys | 142400 | Binqsoft Inc. |
| RRFilterDriverStack_d3.sys | 142300 | Rational Retention |
| cve.sys | 142200 | Absolute Software Corp. |
| spcflt.sys | 142100 | FUJITSU BSC Inc. |
| ldsecusb.sys | 142000 | LANDesk Inc. |
| fencr.sys | 141900 | SODATSW spol. s.r.o. |
| bw_fssec.sys | 141850.5 | Wuhan Buwei Software Technology Co.,Ltd |
| RubiFlt.sys | 141800 | Hitachi, Ltd. |
| NCrypt.sys | 141700 | Nimshi Corp |
| pske.sys | 141661 | Penta Security Systems |
| mfild.sys | 141660 | Penta Security Systems |
| cbfsfilter2017.sys | 141635 | Automaton Inc |
| cbfsfilter2017.sys | 141634 | Automaton Inc |
| cbfsfilter2017.sys | 141633 | Automaton Inc |
| cbfsfilter2017.sys | 141632 | Automaton Inc |
| cbfsfilter2017.sys | 141631 | Automaton Inc |
| cbfsfilter2017.sys | 141630 | Automaton Inc |
| TypeSquare.sys | 141620 | Morisawa inc. |
| xbdocfilter.sys | 141610 | Zrxb |
| EVSDecrypt32.sys | 141600 | Fortium Technologies Ltd |
| EVSDecrypt64.sys | 141600 | Fortium Technologies Ltd |
| EVSDecryptia64.sys | 141600 | Fortium Technologies Ltd |
| T-e.sys | 141550.5 | hdu |
| SophosDt2.sys | 141510 | Sophos Plc |
| afdriver.sys | 141500 | ATUS Technology LLC |
| TrivalentFSFltr.sys | 141430 | Cyber Reliant |
| CmdMnEfs.sys | 141420 | Comodo Security |
| DWENxxxx.sys | 141410 | SciencePark Corporation |
| DWENxxxx.sys | 141400 | SciencePark Corporation |
| westlight.sys | 141350 | Westlight AI |
| hdFileSentryDrv32.sys | 141300 | Heilig Defense |
| hdFileSentryDrv64.sys | 141300 | Heilig Defense |
| SDSCloudDrv.sys | 141255 | Stormshield |
| pnpfs.sys | 141250 | PNP SECURE INC |
| SmartCipherFilter.sys | 141240 | Micro Focus |
| cplcdt2.sys | 141230 | conpal GmbH |
| asCryptoFilter.sys | 141220 | Applied Security GmbH |
| NetCryptKR.sys | 141210 | NetCrypt Pty Ltd |
| SGFS.sys | 141205 | Levyco Development,LLC |
| BHFilter.sys | 141200 | Beachhead Solutions |
| Filecrypt.sys | 141100 | Microsoft |
| encrypt.sys | 141010 | Microsoft |
| swapBuffers.sys | 141000 | Microsoft |

## 130000 - 139999: FSFilter Virtualization

| Minifilter                  | Altitude | Company                                 |
|-----------------------------|----------|-----------------------------------------|
| SkyBLI.sys | 139000.5 | Sky Co.Ltd. |
| Klvirt.sys | 138100 | Kaspersky Lab |
| eseadriver3z.sys | 138080 | ESEA |
| thsmmf.sys | 138060 | Talon Storage Solutions |
| VMagic.sys | 138050 | AI Consulting |
| GetSAS.sys | 138040 | SAS Institute Inc |
| rqtNos.sys | 138030 | ReaQta Ltd. |
| HIPS64.sys | 138020 | Recrypt LLC |
| frxdrv.sys | 138010 | FSLogix Inc. |
| vzdrv.sys | 138000 | Altiris |
| sffsg.sys | 137990 | Starfish Storage Corp |
| AppStream.sys | 137920 | Symantec Corporation |
| Rasm.sys | 137915 | OpDesk Inc |
| boxifier.sys | 137910 | Kenubi |
| xorw.sys | 137900 | CA (XOsoft) |
| ctlua.sys | 137800 | SurfRight B.V. |
| fgccow.sys | 137700 | Fortres Grand Corp. |
| aswSnx.sys | 137600 | ALWIL Software |
| AppIsoFltr.sys | 137500 | Kernel Drivers |
| ptcvfsd.sys | 137400 | PTC |
| CloudFile.sys | 137350.5 | EaseFilter Technologies |
| BDSandBox.sys | 137300 | BitDefender SRL |
| sxfpss-virt.sys | 137200 | Skanix AS |
| DKRtWrt.sys | 137100 | Diskeeper Corporation |
| ivm.sys | 137000 | RingCube Technologies |
| ivm.sys | 136990 | Citrix Systems |
| dtiof.sys | 136900 | Instavia Software Inc. |
| NxTopCP.sys | 136800 | Virtual Ccomputer Inc. |
| svdriver.sys | 136700 | VMware, Inc. |
| AwsEucAppRedirectionDriver.sys | 136680.5 | Amazon Web Services Inc |
| vdpfilefilter.sys | 136660.5 | H3C Ltd. |
| PPnP-LocalBoost2.sys | 136650.5 | Edgeless Opensource Group |
| unifltr.sys | 136600 | Unidesk |
| unidrive.sys (Renamed) | 136600 | Unidesk |
| unirsd.sys | 136600 | Unidesk |
| ive.sys | 136500 | TrendMicro Inc. |
| odamf.sys | 136450 | Sony Corporation |
| SrMxfMf.sys | 136440 | Sony Corporation |
| pszmf.sys | 136430 | Sony Corporation |
| sxsudfmf.sys | 136410 | Sony Corporation |
| vfammf.sys | 136400 | Sony Corporation |
| lwfsflt.sys | 136300 | Liquidware Labs |
| VHDFlt.sys | 136240 | Dell |
| VHDFlt.sys | 136230 | Dell |
| VHDFlt.sys | 136220 | Dell |
| VHDFlt.sys | 136210 | Dell |
| ncfsfltr.sys | 136200 | NComputing Inc. |
| cmdguard.sys | 136100 | COMODO Security Solutions Inc |
| hpfsredir.sys | 136000 | HP |
| svhdxflt.sys | 135100 | Microsoft |
| luafv.sys | 135000 | Microsoft |
| ivm.sys | 134000 | RingCube Technologies |
| ivm.sys | 133990 | Citrix Systems |
| RevBitsEPSMF.sys | 132730.5 | RevBits LLC |
| RasRdpFs.sys | 132720 | Parallels International |
| frxdrvvt.sys | 132700 | FSLogix Inc. |
| pfmfs_???.sys | 132600 | Pismo Technic Inc. |
| Stcvhdmf.sys | 132600 | StorageCraft Tech Corp |
| appdrv01.sys | 132500 | Protection Technology |
| virtual_file.sys | 132400 | Acronis |
| pdiFsFilter.sys | 132300 | Proximal Data Inc. |
| avgvtx86.sys | 132200 | AVG Technologies CZ, s.r.o. |
| avgvtx64.sys | 132200 | AVG Technologies CZ, s.r.o. |
| DataNet_Driver.sys | 132100 | AppSense Ltd |
| EgenPage.sys | 132000 | Egenera, Inc. |
| unidrive.sys-old | 131900 | Unidesk |
| ivm.sys.old | 131800 | RingCube Technologies |
| XiaobaiFsR.sys | 131710 | SHENZHEN UNNOO LTD |
| XiaobaiFs.sys | 131700 | SHENZHEN UNNOO LTD |
| iotfsflt.sys | 131600 | IO Turbine Inc |
| mhpvfs.sys | 131500 | Wunix Limited |
| svdriver.sys | 131400 | SnapVolumes Inc. |
| Sptvrt.sys | 131300 | Safend |
| antirswf.sys | 131210 | Panzor Cybersecurity |
| aicvirt.sys | 131200 | AI Consulting |
| MEMEPMAgent.sys | 130852 | Microsoft |
| sfo.sys | 130100 | Microsoft |
| DeVolume.sys | 130000 | Microsoft |

## 120000 - 129999: FSFilter Physical Quota management

| Minifilter                  | Altitude | Company                                 |
|-----------------------------|----------|-----------------------------------------|
| quota.sys | 125000 | Microsoft |
| qafilter.sys | 124000 | Veritas |
| DroboFlt.sys | 123900 | Data Robotics |

## 100000 - 109999: FSFilter Open File

| Minifilter                  | Altitude | Company                                 |
|-----------------------------|----------|-----------------------------------------|
| insyncmf.sys | 105000 | InSync |
| cbfilter20.sys | 101010 | Bentley Systems Inc |
| SPILock8.sys | 100900 | Software Pursuits Inc. |
| Klbackupflt.sys | 100800 | Kaspersky |
| repkap | 100700 | Vision Solutions |
| symrg.sys | 100600 | Symantec |
| adsfilter.sys | 100500 | PolyServ |
| FMonitor.sys | 100490 | Safetica |
| BFS.sys | 100010 | Microsoft |

## 80000 - 89999: FSFilter Security Enhancer

| Minifilter                  | Altitude | Company                                 |
|-----------------------------|----------|-----------------------------------------|
| TCIJDrv.sys | 88400.5 | Teradyne INC |
| fileWORM.sys | 88350.5 | Fuddata Limited |
| cbfilter20.sys | 88320.5 | MD Anderson Cancer Center |
| KpHrd.sys | 88300 | Ivanti |
| cbfilter20.sys | 88250 | Division-M |
| flflt.sys | 88240.5 | PNP SECURE INC |
| pfcflt.sys | 88240 | PNP SECURE INC |
| arm_minifilter.sys | 88232 | Assured Info Security |
| pegasus.sys | 88230 | Assured Info Security |
| RSBDrv.sys | 88220 | SMTechnology Co. |
| psprotf.sys | 88210 | Panzor Cybersecurity |
| DhtDriver64.sys | 88180.5 | DNP HyperTech Co., Ltd. |
| DhtDriver32.sys | 88180.5 | DNP HyperTech Co., Ltd. |
| ufsf.sys | 88110.5 | media-press.tv S.A. |
| DPMACL.sys | 88100 | Randtronics Pty |
| dsbwnck.sys | 88000 | Easy Solution Inc. |
| cbfilter20.sys | 87911 | Automaton Inc |
| cbfsfilter2017.sys | 87910 | Automaton Inc |
| cbfsfilter2017.sys | 87909 | Automaton Inc |
| cbfsfilter2017.sys | 87908 | Automaton Inc |
| cbfsfilter2017.sys | 87907 | Automaton Inc |
| cbfsfilter2017.sys | 87906 | Automaton Inc |
| cbfsfilter2017.sys | 87905 | Automaton Inc |
| cbfsfilter2017.sys | 87904 | Automaton Inc |
| cbfsfilter2017.sys | 87903 | Automaton Inc |
| cbfsfilter2017.sys | 87902 | Automaton Inc |
| cbfsfilter2017.sys | 87901 | Automaton Inc |
| cbfsfilter2017.sys | 87900 | Automaton Inc |
| RansomStopDriver.sys | 87810 | Maddrix LLC |
| rsbfsfilter.sys | 87800 | Corel Corporation |
| hsmltflt.sys | 87720 | Hitachi Solutions |
| hssfflt.sys | 87710 | Hitachi Solutions |
| acmnflt.sys | 87708 | Hitachi Solutions |
| ACSKFFD.sys | 87700 | Hitachi Solutions |
| MyDLPMF.sys | 87600 | Comodo Group Inc. |
| asioeg.sys | 87550.5 | Encourage Technologies |
| ScuaRaw.sys | 87500 | SCUA Seguran&#231;a da Informa&#231;&#227;o |
| HDSFilter.sys | 87400 | NeoAutus Automation System |
| ikfsmflt.sys | 87300 | IronKey Inc. |
| Klsec.sys | 87200 | Kaspersky Lab |
| XtimUSBFsFilterDrv.sys | 87190 | Dalian CP-SDT Ltd |
| RGFLT_FM.sys | 87180 | Hauri.inc |
| flockflt.sys | 87170 | Ahranta Inc. |
| ZdCore.sys | 87160 | Zends Technological Solutions |
| dcrypt.sys | 87150 | ReactOS Foundation |
| hpradeo.sys | 87140 | Pradeo |
| SDFSAGDRV.SYS | 87130 | ALPS SYSTEM INTERGRATION CO., LTD. |
| SDFSDEVFDRV.SYS | 87120 | ALPS SYSTEM INTERGRATION CO., LTD. |
| SDIFSFDRV.SYS | 87110 | ALPS SYSTEM INTERGRATION CO., LTD. |
| SDFSFDRV.SYS | 87100 | ALPS SYSTEM INTERGRATION CO., LTD. |
| CModule.sys | 87070 | Zhejiang Security Tech |
| HHRRPH.sys | 87010 | H+H Software GmbH |
| HHVolFltr.sys | 87000 | H+H Software GmbH |
| CCRRSecMon.sys | 86960 | Cyber Crucible Inc. |
| RevoNetDriver.sys | 86940.5 | J's Communication Co. |
| SbieDrv.sys | 86900 | Sandboxie L.T.D |
| assetpro.sys | 86800 | pyaprotect&#x2024;com |
| dlp.sys | 86700 | Tellus Software AS |
| eps.sys | 86600 | Lumension Security |
| RapportPG64.sys | 86500 | Trusteer |
| amminifilter.sys | 86400 | AppSense |
| Sniflt.sys | 86300 | Systemneeds, Inc |
| SecFile.sys | 86200 | Secure By Design Inc. |
| philly.sys | 86110 | triCerat Inc. |
| reggy.sys | 86100 | triCerat Inc. |
| cygfilt.sys | 86000 | Livegrid Incorporated |
| prelaunch.sys | 85900 | D3L |
| csareg.sys | 85810 | Cisco Systems |
| csaenh.sys | 85800 | Cisco Systems |
| asi_ns_drv.sys | 85750.5 | ASHINI Co. Ltd. |
| asEpsDrv.sys | 85750 | ASHINI Co. Ltd. |
| CIDACL.sys | 85700 | GE Aviation (Digital Systems Germantown) |
| CVDLP.sys | 85610 | CommVault Systems, Inc. |
| QGPEFlt.sys | 85600 | Quest Software |
| Drveng.sys | 85500 | CA |
| PPDMFilter_x64.sys | 85550.5 | PolicyPak Software Inc |
| PPDMFilter_x86.sys | 85550.5 | PolicyPak Software Inc |
| vracfil2.sys | 85400 | HAURI |
| TFsDisk.sys | 85300 | Teruten |
| rcMiniDrv.sys | 85200 | REDGATE CO.,LTD. |
| SnMc5xx.sys | 85100 | Informzaschita |
| FSPFltd.sys | 85010 | Alfa |
| AifaFFP.sys | 85000 | Alfa |
| EsAccCtlFE.sys | 84901 | EgoSecure GmbH |
| DpAccCtl.sys | 84900 | Softbroker GmbH |
| privman.sys | 84800 | BeyondTrust |
| eumntvol.sys | 84700 | Eugrid Inc |
| SoloEncFilter.sys | 84600 | Soliton Systems |
| sbfilter.sys | 84500 | UC4 Sofware |
| cposfw.sys | 84450 | Check Point Software Technologies Ltd |
| vsdatant.sys | 84400 | Zone Labs LLC |
| SePnet.sys | 84350 | Humming Heads, Inc. |
| SePuld.sys | 84340 | Humming Heads, Inc. |
| SePpld.sys | 84330 | Humming Heads, Inc. |
| SePfsd.sys | 84320 | Humming Heads, Inc. |
| SePwld.sys | 84310 | Humming Heads, Inc. |
| SePprd.sys | 84300 | Humming Heads, Inc. |
| InPFlter.sys | 84200 | Humming Heads, Inc. |
| CProCtrl.sys | 84100 | Crypto-Pro |
| spyshelter.sys | 84000 | Datpol |
| clpinspprot.sys | 83900 | Information Technology Company Ltd. |
| AbrEpm.sys | 83800 | FastTrack Software ApS |
| uvmfsflt.sys | 83376 | NEC Corporation  |
| ipm.sys | 82870.5 | Virsec Systems Inc. |
| ProtectIt.sys | 82373 | TeraByte Inc. |
| dguard.sys | 82300 | Dmitry Varshavsky |
| NSUSBStorageFilter.sys | 82200 | NetSupport Ltd |
| RMSEFFMV.SYS | 82100 | CJSC Returnil Software |
| BoksFLAC.sys | 82000 | Fox Technologies |
| cpAcOnPnP.sys | 81910 | conpal GmbH |
| cpsgfsmf.sys | 81900 | conpal GmbH |
| ndevsec.sys | 81800 | Norman ASA |
| ViewIntus_RTDG.sys | 81700 | Pentego Technologies Ltd |
| BKSandFS.sys | 81640 | Binklac Workstation |
| BWAnticheat.sys | 81638 | Binklac Workstation |
| airlock.sys | 81630 | Airlock Digital Pty Ltd |
| zam.sys | 81620 |  |
| ANXfsm.sys | 81610 | Arcdo |
| CDrSDFlt.sys | 81600 | Arcdo |
| crnselfdefence32.sys | 81500 | Coranti Inc. |
| crnselfdefence64.sys | 81500 | Coranti Inc. |
| zlock_drv.sys | 81400 | SecurIT |
| f101fs.sys | 81300 | Fortres Grand Corp. |
| sysgar.sys | 81200 | Nucleus Data Recover |
| EmbargoM.sys | 81100 | ScriptLogic |
| KSkyMonitor.sys | 81080 | Sky Monitor |
| ngssdef.sys | 81050 | Wontok Inc |
| ssb.sys | 81041 | Wontok Inc |
| regflt.sys | 81040 | Wontok Inc |
| fsds2a.sys | 81000 | Splitstreem Ltd |
| HeimdalInsights.sys | 80950.5 | Heimdal Security A/S |
| csacentr.sys | 80900 | Cisco Systems |
| ScvFLT50.sys | 80850 | Secuve Ltd |
| paritydriver.sys | 80800 | Bit9, Inc. |
| nkfsprot.sys | 80710 | Konneka |
| nkprot.sys | 80700 | KONNEKA Information Technologies |
| acpadlock.sys | 80691 | IntSoft Co., Ltd |
| ksmf.sys | 80690 | IntSoft Co., Ltd |
| amsdk.sys | 80682.5 | WatchDogDevelopment.com, LLC |
| im.sys | 80680 | CrowdStrike |
| SophosED.sys | 80670 | Sophos |
| jazzfile.sys | 80660 | Jazz Networks |
| SMXFs.sys | 80500 | OSR |

## 60000 - 69999: FSFilter Copy Protection

| Minifilter                  | Altitude | Company                                 |
|-----------------------------|----------|-----------------------------------------|
| plypFsMon.sys | 67100 | PolyPort Inc. |
| d3clock.sys | 67000 | D3CRYPT3D LLC |
| cbfltfs4.sys | 66500 | I3D Technology Inc |
| CkProcess.sys | 66100 | KASHU SYSTEM DESIGN INC. |
| dlmfprot.sys | 66000 | Data Encrypt Sys |
| baprtsef.sys | 65700 | BitArmor Systems, Inc |
| sxfpss.sys | 65600 | Skanix AS |
| rgasdev.sys | 65500 | Macrovision |
| SkyFPDrv.sys | 65410 | Sky Co. Ltd. |
| SkyLWP.sys | 65400 | Sky Co. Ltd. |
| SkySDVRF.sys | 65390 | Sky Co. Ltd. |
| SnEraser.sys | 65300 | Informzaschita |
| vfilter.sys | 65200 | RSJ Software GmbH |
| COGOFlt32.sys | 65100 | Fortium Technologies Ltd |
| COGOFlt64.sys | 65100 | Fortium Technologies Ltd |
| COGOFLTia64.sys | 65100 | Fortium Technologies Ltd |
| scrubber.sys | 65000 | Microsoft |
| SmDLP.sys | 64100 | SmTools |
| BRDriver.sys | 64000 | BitRaider LLC |
| BRDriver64.sys | 64000 | BitRaider LLC |
| X7Ex.sys | 62500 | Exent Technologies Ltd |
| LibertyFSF.sys | 62300 | Bayalink Solutions Co |
| axfsdrv2.sys | 62100 | Axence Software Inc. |
| sds.sys | 62000 | Egress Software |
| zzenc.sys | 61650.5 | Imdtech LLC |
| TotalSystemAuditor.sys | 61600 | ANRC LLC |
| MBAMApiary.sys | 61500 | Malwarebytes Corp. |
| WA_FSW.sys | 61400 | Programas Administraci&#243;n y Mejoramiento |
| ViewIntus_RTAS | 61300 | Pentego Technologies |
| tffac.sys | 61200 | Toshiba Corporation |
| tccp.sys | 61100 | TrusCont Ltd |
| KomFS.sys | 61000 | KOM Networks |

## 40000 - 49999: FSFilter Bottom

| Minifilter                  | Altitude | Company                                 |
|-----------------------------|----------|-----------------------------------------|
| RMPFileMounter.sys | 48000 | ManageEngine Zoho |
| MFPAMCtrl.sys | 47500 | Micro Focus |
| cbfsfilter2017.sys | 47400 | 12d Synergy |
| pfmfs_???.sys | 47300 | Pismo Technic Inc. |
| AlfaVS.sys | 47290.5 | AlfaSP.com |
| DLDriverMiniFlt.sys | 47200 | Acronis |
| DLPDriverProt.sys | 47199.5 | Acronis |
| hsmltlib.sys | 47110 | Hitachi Solutions |
| hskdlib.sys | 47100 | Hitachi Solutions |
| acmnlib.sys | 47090 | Hitachi Solutions |
| aictracedrv_b.sys | 47000 | AI Consulting |
| SBox.sys | 46950 | ASF Labs 2019 LTD |
| hhdcfltr.sys | 46900 | Seagate Technology |
| AmdFSMini.sys | 46890.5 | Advanced Micro Devices |
| Npsvctrig.sys | 46000 | Microsoft |
| klvfs.sys | 44900 | Kaspersky Lab |
| klbackupflt.sys | 44890 | Kaspersky Lab |
| rsfxdrv.sys | 41000 | Microsoft |
| defilter.sys | 40900 | Microsoft |
| AppVVemgr.sys | 40800 | Microsoft |
| wofadk.sys | 40730 | Microsoft |
| wof.sys | 40700 | Microsoft |
| fileinfo | 40500 | Microsoft |
| WinSetupBoot.sys | 40400 | Microsoft |
| WinSetupMon.sys | 40300 | Microsoft |

## 20000 - 29999: FSFilter System

None.
