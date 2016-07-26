---
title: Allocated Altitudes
author: windows-driver-content
description: Allocated Altitudes
ms.assetid: EC1993FB-5219-4C0C-A76A-05937A461C5A
---

# Allocated Altitudes


A file system minifilter driver developed to the Filter Manager model must have a unique identifier called an altitude that defines its position relative to other minifilters present in the file system stack. Minifilter altitudes are allocated by Microsoft based on minifilter requirements and load order group.

The current altitude allocations are listed for each of the following load order groups.

## <span id="420000_-_429999__Filter"></span><span id="420000_-_429999__filter"></span><span id="420000_-_429999__FILTER"></span>420000 - 429999: Filter


| Minifilter   | Altitude | Company   |
|--------------|----------|-----------|
| ntoskrnl.exe | 425500   | Microsoft |
| ntoskrnl.exe | 425000   | Microsoft |

 

## <span id="400000_-_409999__FSFilter_Top"></span><span id="400000_-_409999__fsfilter_top"></span><span id="400000_-_409999__FSFILTER_TOP"></span>400000 - 409999: FSFilter Top


| Minifilter                    | Altitude | Company                  |
|-------------------------------|----------|--------------------------|
| ioqos.sys                     | 409000   | Microsoft                |
| fsdepends.sys                 | 407000   | Microsoft                |
| sftredir.sys                  | 406000   | Microsoft                |
| dfs.sys                       | 405000   | Microsoft                |
| csvnsflt.sys                  | 404900   | Microsoft                |
| csvflt.sys                    | 404800   | Microsoft                |
| Microsoft.Uev.AgentDriver.sys | 404710   | Microsoft                |
| AppvVfs.sys                   | 404700   | Microsoft                |
| eaw.sys                       | 401900   | Raytheon Cyber Solutions |
| TVFsfilter.sys                | 401800   | TrustView                |
| KKDiskProtecter.sys           | 401700   | Goldmsg                  |
| AgentComm.sys                 | 401600   | Trustwave Holding        |
| rvsavd.sys                    | 401500   | CJSC Returnil Software   |
| dgdmk.sys                     | 401400   | Verdasys Inc.            |
| tusbstorfilt.sys              | 401300   | SimplyCore LLC           |
| pcgenfam.sys                  | 401200   | Soluto                   |
| atrsdfw.sys                   | 401100   | Altiris                  |
| tpfilter.sys                  | 401000   | RedPhone Security        |
| mbamwatchdog.sys              | 400900   | Malwarebytes Corporation |
| edevmon.sys                   | 400800   | ESET                     |
| vmwflstor.sys                 | 400700   | VMware, Inc.             |

 

## <span id="_360000_-_389999__FSFilter_Activity_Monitor"></span><span id="_360000_-_389999__fsfilter_activity_monitor"></span><span id="_360000_-_389999__FSFILTER_ACTIVITY_MONITOR"></span> 360000 - 389999: FSFilter Activity Monitor


| Minifilter                       | Altitude | Company                                                |
|----------------------------------|----------|--------------------------------------------------------|
| DhWatchdog.sys                   | 389030   | Microsoft                                              |
| NpEtw.sys                        | 389020   | Koby Kahane                                            |
| OczMiniFilter.sys                | 389010   | OCZ Storage                                            |
| ielcp.sys                        | 389004   | Intel Corporation                                      |
| IESlp.sys                        | 389002   | Intel Corporation                                      |
| IntelCAS.sys                     | 389000   | Intel Corporation                                      |
| boxifier.sys                     | 388990   | Kenubi                                                 |
| SamsungRapidFSFltr.sys           | 388980   | NVELO                                                  |
| drsfile.sys                      | 388970   | MRY Inc.                                               |
| CrUnCopy.sys                     | 388964   | Shenzhen CloudRiver                                    |
| aictracedrv\_am.sys              | 388960   | AI Consulting                                          |
| fcontrol.sys                     | 388950   | SODATSW spol. s r.o.                                   |
| qfilter.sys                      | 388940   | Quorum Labs                                            |
| Redlight.sys                     | 388930   | Trustware Ltd                                          |
| eps.sys                          | 388920   | Lumension                                              |
| VHDTrack.sys                     | 388915   | Intronis Inc                                           |
| VHDDelta.sys                     | 388912   | Niriva LLC                                             |
| FSTrace.sys                      | 388910   | Niriva LLC                                             |
| YahooStorage.sys                 | 388900   | Yahoo Japan Corporation                                |
| KeWF.sys                         | 388890   | KEBA AG                                                |
| epregflt.sys                     | 388888   | Check Point Software                                   |
| zsfprt.sys                       | 388880   | k4solution Co.                                         |
| dsflt.sys                        | 388876   | cEncrypt                                               |
| bfaccess.sys                     | 388872   | bitFence Inc.                                          |
| xcpl.sys                         | 388870   | X-Cloud Systems                                        |
| EaseFlt.sys                      | 388860   | EaseVault Technologies Inc.                            |
| sieflt.sys                       | 388852   | Quick Heal Technologies Pvt. Ltd.                      |
| cssdlp.sys                       | 388851   | Quick Heal Technologies Pvt. Ltd.                      |
| cssdlp.sys                       | 388850   | CoSoSys                                                |
| INISBDrv64.sys                   | 388840   | Initech Inc.                                           |
| trace.sys                        | 388831   | Fitsec Ltd                                             |
| SandDriver.sys                   | 388830   | Fitsec Ltd                                             |
| dskmn.sys                        | 388820   | Honeycomb Technologies                                 |
| xkfsfd.sys                       | 388810   | Jiransoft Co., Ltd                                     |
| pcpifd.sys                       | 388800   | Jiransoft Co., Ltd                                     |
| NNTInfo.sys                      | 388790   | New Net Technologies Limited                           |
| FsMonitor.sys                    | 388780   | IBM                                                    |
| CVCBT.sys                        | 388770   | CommVault Systems, Inc.                                |
| AwareCore.sys                    | 388760   | TaaSera                                                |
| laFS.sys                         | 388750   | NetworkProfi Ltd.                                      |
| fsnk.sys                         | 388740   | SoftPerfect Research                                   |
| RGNT.sys                         | 388730   | HFN                                                    |
| fltRs329.sys                     | 388720   | Secured Globe Inc.                                     |
| ospmon.sys                       | 388710   | SC ODEKIN SOLUTIONS SRL                                |
| edsigk.sys                       | 388700   | Enterprise Data Solutions, Inc.                        |
| fiometer.sys                     | 388692   | Fusion-io                                              |
| dcSnapRestore.sys                | 388690   | Fusion-io                                              |
| fam.sys                          | 388680   | Quick Heal Technologies Pvt. Ltd.                      |
| Tritiumfltr.sys                  | 388670   | Tritium Inc.                                           |
| BlackbirdFSA.sys                 | 388650   | BeyondTrust Inc.                                       |
| hfileflt.sys                     | 388640   | Trend Micro Inc.                                       |
| TMUMH.sys                        | 388630   | Trend Micro Inc.                                       |
| AcDriver.sys                     | 388620   | Trend Micro, Inc.                                      |
| SakFile.sys                      | 388610   | Trend Micro, Inc.                                      |
| SakMFile.sys                     | 388600   | Trend Micro, Inc.                                      |
| airlock.sys                      | 388570   | Airlock Digital Pty Ltd                                |
| kmNWCH.sys                       | 388560   | IGLOO SECURITY, Inc.                                   |
| ISIRMFmon.sys                    | 388550   | ALPS SYSTEM INTERGRATION CO.                           |
| heimdall.sys                     | 388540   | Arkoon Network Security                                |
| thetta.sys                       | 388530   | Syncopate                                              |
| DTPL.sys                         | 388520   | CONNECT SHIFT LTD                                      |
| CyProtectDrv32.sys               | 388510   | Cylance Inc.                                           |
| CyProtectDrv64.sys               | 388510   | Cylance Inc.                                           |
| tbfsfilt.sys                     | 388500   | Third Brigade                                          |
| LDSecDrv.sys                     | 388490   | LANDESK Software                                       |
| SGResFlt.sys                     | 388480   | Samsung SDS Ltd                                        |
| CwMem2k64.sys                    | 388470   | ApSoft                                                 |
| axfltdrv.sys                     | 388460   | Axact Pvt Ltd                                          |
| RMDiskMon.sys                    | 388450   | Qingdao Ruanmei Network Technology Co.                 |
| diskactmon.sys                   | 388440   | Qingdao Ruanmei Network Technology Co.                 |
| Codex.sys                        | 388430   | GameHi Co.                                             |
| CatMF.sys                        | 388420   | Logichron                                              |
| RW7FsFlt.sys                     | 388410   | PJSC KP VTI                                            |
| aswFsBlk.sys                     | 388400   | ALWIL Software                                         |
| libwamf.sys                      | 388350   | OPSWAT Inc.                                            |
| szdfmdrv.sys                     | 388340   | SaferZone Co.                                          |
| sprtdrv.sys                      | 388330   | SaferZone Co.                                          |
| SWFsFltr.sys                     | 388320   | Solarwinds LLC                                         |
| flashaccelfs.sys                 | 388310   | Network Appliance                                      |
| changelog.sys                    | 388300   | Network Appliance                                      |
| TGFSMF.sys                       | 388200   | Tetraglyph Technologies                                |
| evscase.sys                      | 388100   | March Hare Software Ltd                                |
| tsifilemon.sys                   | 388012   | Intercom                                               |
| MarSpy.sys                       | 388010   | Intercom                                               |
| BrnFileLock.sys                  | 388000   | Blue Ridge Networks                                    |
| BrnSecLock.sys                   | 387990   | Blue Ridge Networks                                    |
| LCgAdMon.sys                     | 387977   | YATEM Co. Ltd.                                         |
| LCmAdMon.sys                     | 387976   | YATEM Co. Ltd.                                         |
| LCgFileMon.sys                   | 387975   | YATEM Co. Ltd.                                         |
| LCmFile.sys                      | 387974   | YATEM Co. Ltd.                                         |
| LCgFile.sys                      | 387972   | YATEM Co. Ltd.                                         |
| LCmFileMon.sys                   | 387970   | YATEM Co. Ltd.                                         |
| IridiumSwitch.sys                | 387960   | Confio                                                 |
| scensemon.sys                    | 387950   | Scense                                                 |
| ruaff.sys                        | 387940   | RUNEXY                                                 |
| bbfilter.sys                     | 387930   | derivo GmbH                                            |
| Bfmon.sys                        | 387920   | Baidu (Hong Kong) Limited                              |
| BdRdFolder.sys                   | 387910   | Baidu (beijing)                                        |
| pscff.sys                        | 387900   | Weing Co.,Ltd.                                         |
| fcnotify.sys                     | 387880   | TCXA Ltd.                                              |
| aaf.sys                          | 387860   | Actifio Inc                                            |
| gddcv.sys                        | 387840   | G Data Software AG                                     |
| wgfile.sys                       | 387820   | ORANGE WERKS Inc                                       |
| zesfsmf.sys                      | 387800   | Novell                                                 |
| uamflt.sys                       | 387700   | Sevtechnotrans                                         |
| ehdrv.sys                        | 387600   | ESET, spol. s r.o.                                     |
| Snilog.sys                       | 387500   | Systemneeds, Inc                                       |
| tss.sys                          | 387400   | Tiversa Inc                                            |
| bapfecpt.sys                     | 387310   | BitArmor Systems, Inc                                  |
| bamfltr.sys                      | 387300   | BitArmor Systems, Inc                                  |
| TrustedEdgeFfd.sys               | 387200   | FileTek, Inc.                                          |
| MRxGoogle.sys                    | 387100   | Google, Inc.                                           |
| YFSDR.SYS                        | 387010   | Yokogawa R&L Corp                                      |
| YFSD.SYS                         | 387000   | Yokogawa R&L Corp                                      |
| YFSRD.sys                        | 386990   | Yokogawa R&L Corp                                      |
| USBPDH.SYS                       | 386901   | Centre for Development of Advanced Computing           |
| pecfilter.sys                    | 386900   | C-DAC Hyderabad                                        |
| GKPFCB.sys                       | 386810   | INCA Internet Co.                                      |
| GKPFCB64.sys                     | 386810   | INCA Internet Co.                                      |
| TkPcFtCb.sys on 32bit            | 386800   | INCA Internet Co.,Ltd.                                 |
| TkPcFtCb64.sys on 64bit          | 386800   | INCA Internet Co.,Ltd.                                 |
| bmregdrv.sys                     | 386731   | Yandex LLC                                             |
| bmfsdrv.sys                      | 386730   | Yandex LLC                                             |
| CarbonBlackK.sys                 | 386720   | Bit9 Inc.                                              |
| ScAuthFSFlt.sys                  | 386710   | Security Code LLC                                      |
| ScAuthIoDrv.sys                  | 386700   | Security Code LLC                                      |
| mfeaskm.sys                      | 386610   | McAfee                                                 |
| mfencfilter.sys                  | 386600   | McAfee                                                 |
| WinFLAHdrv.sys                   | 386540   | NewSoftwares.net                                       |
| WinFLAdrv.sys                    | 386530   | NewSoftwares.net                                       |
| WinDBdrv.sys                     | 386520   | NewSoftwares.net,Inc.                                  |
| WinFLdrv.sys                     | 386510   | NewSoftwares.net,Inc.                                  |
| WinFPdrv.sys                     | 386500   | NewSoftwares.net,Inc.                                  |
| SkyAMDrv.sys                     | 386430   | Sky Co.                                                |
| arta.sys                         | 386420   | SheedSoft Ltd.                                         |
| ApexSqlFilterDriver.sys          | 386410   | ApexSQL LLC                                            |
| stflt.sys                        | 386400   | Xacti                                                  |
| tbrdrv.sys                       | 386390   | Crawler Group                                          |
| WinTeonMiniFilter.sys            | 386320   | Dmitry Stefankov                                       |
| wiper.sys                        | 386310   | Dmitry Stefankov                                       |
| DevMonMiniFilter.sys             | 386300   | Dmitry Stefankov                                       |
| VMWVvpfsd.sys                    | 386200   | VMware, Inc.                                           |
| RTOLogon.sys (Renamed)           | 386200   | VMware, Inc.                                           |
| FileGuard.sys                    | 386140   | RES Software                                           |
| NetGuard.sys                     | 386130   | RES Software                                           |
| RegGuard.sys                     | 386120   | RES Software                                           |
| ImgGuard.sys                     | 386110   | RES Software                                           |
| AppGuard.sys                     | 386100   | RES Software                                           |
| cpepmon.sys                      | 386010   | Checkpoint Software                                    |
| CGWMF.sys                        | 386000   | NetIQ                                                  |
| ISRegFlt.sys                     | 385990   | Flexera Software                                       |
| ISRegFlt64.sys                   | 385990   | Flexera Software                                       |
| immflex.sys                      | 385910   | Immidio B.V.                                           |
| StegoProtect.sys                 | 385900   | Stegosystems                                           |
| brfilter.sys                     | 385890   | Bromium Inc                                            |
| secRMM.sys                       | 385880   | Squadra Technologies                                   |
| dgfilter.sys                     | 385870   | DataGravity Inc.                                       |
| Backupreader.sys                 | 385500   | Microsoft                                              |
| AppVMon.sys                      | 385400   | Microsoft                                              |
| DpmFilter.sys                    | 385300   | Microsoft                                              |
| Procmon11.sys                    | 385200   | Microsoft                                              |
| minispy.sys - Top                | 385100   | Microsoft                                              |
| fdrtrace.sys                     | 385001   | Microsoft                                              |
| filetrace.sys                    | 385000   | Microsoft                                              |
| uwfreg.sys                       | 384910   | Microsoft                                              |
| uwfs.sys                         | 384900   | Microsoft                                              |
| AeFilter.sys                     | 383310   | Faronics Corporation                                   |
| QQProtect.sys                    | 383300   | Tencent (Shenzhen)                                     |
| QQProtectX64.sys                 | 383300   | Tencent (Shenzhen)                                     |
| groundling32.sys                 | 383200   | Dell Secureworks                                       |
| groundling64.sys                 | 383200   | Dell Secureworks                                       |
| avgtpx86.sys                     | 383190   | AVG Technologies CZ                                    |
| avgtpx64.sys                     | 383190   | AVG Technologies CZ                                    |
| DataNow\_Driver.sys              | 383182   | AppSense Ltd                                           |
| UcaFltDriver.sys                 | 383180   | AppSense Ltd                                           |
| YFSD2.sys                        | 383170   | Yokogawa Corpration                                    |
| Kisknl.sys                       | 383160   | kingsoft                                               |
| MWatcher.sys                     | 383150   | Neowiz Corporation                                     |
| tsifilemon.sys                   | 383140   | Intercom                                               |
| FIM.sys                          | 383130   | eIQnetworks                                            |
| cFSfdrv                          | 383120   | Chaewool                                               |
| ajfsprot.sys                     | 383110   | Analytik Jena AG                                       |
| isafermon                        | 383100   | (c)SMS                                                 |
| kfac.sys                         | 383000   | Beijing CA-JinChen Software Co.                        |
| FJGSDis2.sys                     | 382900   | FUJITSU LIMITED                                        |
| zqFilter                         | 382800   | magrasoft Ltd                                          |
| ntps\_fa.sys                     | 382700   | NTP Software                                           |
| sConnect.sys                     | 382600   | I-O DATA DEVICE                                        |
| AdaptivaClientCache32.sys        | 382500   | Adaptiva                                               |
| AdaptivaclientCache64.sys        | 382500   | Adaptiva                                               |
| GoFSMF.sys                       | 382430   | Gorizonty Rosta Ltd                                    |
| SWCommFltr.sys                   | 382420   | SnoopWall LLC                                          |
| atflt.sys                        | 382410   | Atlansys Software                                      |
| amfd.sys                         | 382400   | Atlansys Software                                      |
| iSafeKrnl.sys                    | 382390   | Elex Tech Inc                                          |
| iSafeKrnlMon.sys                 | 382380   | Elex Tech Inc                                          |
| 360box.sys                       | 382310   | Qihoo 360                                              |
| 360fsflt.sys                     | 382300   | Beijing Qihoo Technology Co.                           |
| scred.sys                        | 382210   | SoftCamp Co.                                           |
| PDGenFam.sys                     | 382200   | Soluto LTD                                             |
| MCFileMon64.sys (x64 systems)    | 382100   | Sumitomo Electric Ltd.                                 |
| MCFileMon32.sys (x32 systems)    | 382100   | Sumitomo Electric Ltd.                                 |
| RyGuard.sys                      | 382050   | SHENZHEN UNNOO Information Techco.                     |
| FileShareMon.sys                 | 382040   | SHENZHEN UNNOO Information Techco.                     |
| ryfilter.sys                     | 382030   | SHENZHEN UNNOO Information Techco.                     |
| secufile.sys                     | 382020   | Shenzhen Unnoo LTD                                     |
| XiaobaiFs.sys                    | 382010   | Shenzhen Unnoo LTD                                     |
| XiaobaiFsR.sys                   | 382000   | Shenzhen Unnoo LTD                                     |
| TWBDCFilter.sys                  | 381910   | Trustwave                                              |
| VPDrvNt.sys                      | 381900   | AhnLab, Inc.                                           |
| eetd32.sys                       | 381800   | Entrust Inc.                                           |
| eetd64.sys                       | 381800   | Entrust Inc.                                           |
| dnaFSMonitor.sys                 | 381700   | Dtex Systems                                           |
| iwhlp2.sys on 2000               | 381610   | InfoWatch                                              |
| iwhlpxp.sys on XP                | 381610   | InfoWatch                                              |
| iwhlp.sys on Vista               | 381610   | InfoWatch                                              |
| iwdmfs.sys                       | 381600   | InfoWatch                                              |
| IronGateFD.sys                   | 381500   | rubysoft                                               |
| MagicBackupMonitor.sys           | 381400   | Magic Softworks, Inc.                                  |
| Sonar.sys                        | 381337   | IKARUS Security                                        |
| IPFilter.sys                     | 381310   | Jinfengshuntai                                         |
| MSpy.sys                         | 381300   | Ladislav Zezula                                        |
| inuse.sys                        | 381200   | March Hare Software Ltd                                |
| flyfs.sys                        | 381160   | NEC Soft                                               |
| serfs.sys                        | 381150   | NEC Soft                                               |
| hdrfs.sys                        | 381140   | NEC Soft                                               |
| UVMCIFSF.sys                     | 381130   | NEC Corporation                                        |
| ICFClientFlt.sys                 | 381120   | NEC System Technologies,Ltd.                           |
| IccFileIoAd.sys                  | 381110   | NEC System Technologies,Ltd.                           |
| IccFilterAudit.sys               | 381100   | NEC System Technologies                                |
| mtsvcdf.sys                      | 381000   | CristaLink                                             |
| SQLsafeFilterDriver.sys          | 380901   | Idera Software                                         |
| IderaFilterDriver.sys            | 380900   | Idera                                                  |
| xhunter1.sys                     | 380800   | Wellbia.com                                            |
| PkgFilter.sys                    | 380700   | Scalable Software                                      |
| snimg.sys                        | 380600   | Softnext Technologies                                  |
| KC3.sys                          | 380500   | Infotecs                                               |
| CbSampleDrv.sys                  | 380020   | Microsoft                                              |
| CbSampleDrv.sys                  | 380010   | Microsoft                                              |
| CbSampleDrv.sys                  | 380000   | Microsoft                                              |
| simrep.sys                       | 371100   | Microsoft                                              |
| change.sys                       | 370160   | Microsoft                                              |
| delete\_flt.sys                  | 370150   | Microsoft                                              |
| SmbResilFilter.sys               | 370140   | Microsoft                                              |
| usbtest.sys                      | 370130   | Microsoft                                              |
| NameChanger.sys                  | 370120   | Microsoft                                              |
| failMount.sys                    | 370110   | Microsoft                                              |
| failAttach.sys                   | 370100   | Microsoft                                              |
| stest.sys                        | 370090   | Microsoft                                              |
| cdo.sys                          | 370080   | Microsoft                                              |
| ctx.sys                          | 370070   | Microsoft                                              |
| fmm.sys                          | 370060   | Microsoft                                              |
| cancelSafe.sys                   | 370050   | Microsoft                                              |
| message.sys                      | 370040   | Microsoft                                              |
| passThrough.sys                  | 370030   | Microsoft                                              |
| nullFilter.sys                   | 370020   | Microsoft                                              |
| ntest.sys                        | 370010   | Microsoft                                              |
| minispy.sys - Middle             | 370000   | Microsoft                                              |
| docvmonk.sys                     | 368380   | NURILAB                                                |
| docvmonk64.sys                   | 368380   | NURILAB                                                |
| InvProtectDrv.sys                | 368370   | Invincea                                               |
| InvProtectDrv64.sys              | 368370   | Invincea                                               |
| browserMon.sys                   | 368360   | Adtrustmedia                                           |
| SfdFilter.sys                    | 368350   | Sandoll Communication                                  |
| phdcbtdrv.sys                    | 368340   | PHD Virtual Tech Inc.                                  |
| sysdiag.sys                      | 368330   | HeroBravo Technology                                   |
| cfrmd.sys                        | 368320   | Comodo Security Solutions                              |
| repdrv.sys                       | 368310   | Vision Solutions                                       |
| repmon.sys                       | 368300   | Vision Solutions                                       |
| cvofflineFlt32.sys               | 368200   | Quantum Corporation.                                   |
| cvofflineFlt64.sys               | 368200   | Quantum Corporation.                                   |
| DsDriver.sys                     | 368100   | Warp Disk Software                                     |
| nlcbhelpx86.sys                  | 368000   | NetLib                                                 |
| nlcbhelpx64.sys                  | 368000   | NetLib                                                 |
| nlcbhelpi64.sys                  | 368000   | NetLib                                                 |
| wbfilter.sys                     | 367950   | Whitebox Security                                      |
| LRAgentMF.sys                    | 367900   | LogRhythm                                              |
| Drwebfwflt.sys                   | 367810   | Doctor Web                                             |
| EventMon.sys                     | 367800   | Doctor Web                                             |
| soidriver.sys                    | 367750   | Sophos Plc                                             |
| drvhookcsmf.sys                  | 367700   | GrammaTech, Inc.                                       |
| drvhookcsmf\_amd64.sys           | 367700   | GrammaTech, Inc.                                       |
| avipbb.sys                       | 367600   | Avira GmbH                                             |
| FileSightMF.sys                  | 367500   | PA File Sight                                          |
| csaam.sys                        | 367400   | Cisco Systems                                          |
| FSMon.sys                        | 367300   | 1mill                                                  |
| mfl.sys                          | 367200   | OSR Open Systems Resources, Inc.                       |
| filefilter.sys                   | 367100   | Beijing Zhong Hang Jiaxin Computer Technology Co.,Ltd. |
| iiscache.sys                     | 367000   | Microsoft                                              |
| nowonmf.sys                      | 366993   | Diskeeper Corporation                                  |
| dktlfsmf.sys                     | 366992   | Diskeeper Corporation                                  |
| DKDrv.sys                        | 366991   | Diskeeper Corporation                                  |
| DKRtWrt.sys - temp fix for XPSP3 | 366990   | Diskeeper Corporation                                  |
| HBFSFltr.sys                     | 366980   | Diskeeper Corporation                                  |
| xoiv8x64.sys                     | 366940   | Arcserve                                               |
| xomfcbt8x64.sys                  | 366930   | CA                                                     |
| KmxAgent.sys                     | 366920   | CA                                                     |
| KmxFile.sys                      | 366910   | CA                                                     |
| KmxSbx.sys                       | 366900   | CA                                                     |
| PointGuardVistaR32.sys           | 366810   | Futuresoft                                             |
| PointGuardVistaR64.sys           | 366810   | Futuresoft                                             |
| PointGuardVistaF.sys             | 366800   | Futuresoft                                             |
| PointGuardVista64F.sys           | 366800   | Futuresoft                                             |
| vintmfs.sys                      | 366789   | CondusivTechnologies                                   |
| hiofs.sys                        | 366782   | Condusiv Technologies                                  |
| intmfs.sys                       | 366781   | CondusivTechnologies                                   |
| excfs.sys                        | 366780   | CondusivTechnologies                                   |
| zampit\_ml.sys                   | 366700   | Zampit                                                 |
| rflog.sys                        | 366600   | AppStream, Inc.                                        |
| LivedriveFilter.sys              | 366500   | Livedrive Internet Ltd                                 |
| regmonex.sys                     | 366410   | Tranxition Corp                                        |
| TXRegMon.sys                     | 366400   | Tranxition Corp                                        |
| SDVFilter.sys                    | 366300   | Soliton Systems K.K.                                   |
| eLock2FSCTLDriver.sys            | 366210   | Egis Technology Inc.                                   |
| msiodrv4.sys                     | 366200   | Centennial Software Ltd                                |
| mmPsy32.sys                      | 366110   | Resplendence Software Projects                         |
| mmPsy64.sys                      | 366110   | Resplendence Software Projects                         |
| rrMon32.sys                      | 366100   | Resplendence Software Projects                         |
| rrMon64.sys                      | 366100   | Resplendence Software Projects                         |
| cvsflt.sys                       | 366000   | March Hare Software Ltd                                |
| ktsyncfsflt.sys                  | 365920   | KnowledgeTree Inc.                                     |
| nvmon.sys                        | 365900   | NetVision, Inc.                                        |
| SnDacs.sys                       | 365810   | Informzaschita                                         |
| SnExequota.sys                   | 365800   | Informzaschita                                         |
| llfilter.sys                     | 365700   | SecureAxis Software                                    |
| hafsnk.sys                       | 365660   | HA Unix Pt                                             |
| BWFSDrv.sys                      | 365650   | Quest Software Inc.                                    |
| QFAPFlt.sys                      | 365600   | Quest Software                                         |
| XendowFLT.sys                    | 365570   | Credant Technologies                                   |
| fmdrive.sys                      | 365500   | Cigital, Inc.                                          |
| EGMinFlt.sys                     | 365400   | WhiteCell Software Inc.                                |
| it2drv.sys                       | 365310   | Soliton Systems                                        |
| solitkm.sys                      | 365300   | Soliton Systems                                        |
| pgpwdefs.sys                     | 365270   | Symantec                                               |
| GEProtection.sys                 | 365260   | Symantec                                               |
| diflt.sys                        | 365260   | Symantec Corp.                                         |
| sysMon.sys                       | 365250   | Symantec                                               |
| ssrfsf.sys                       | 365210   | Symantec                                               |
| emxdrv2.sys                      | 365200   | Symantec                                               |
| reghook.sys                      | 365150   | Symantec                                               |
| spbbcdrv.sys                     | 365100   | Symantec                                               |
| bhdrvx86.sys                     | 365100   | Symantec                                               |
| bhdrvx64.sys                     | 365100   | Symantec                                               |
| SISIPSFileFilter                 | 365010   | Symantec                                               |
| symevent.sys                     | 365000   | Symantec                                               |
| wrpfv.sys                        | 364900   | Microsoft                                              |
| usbl\_ifsfltr.sys                | 364800   | SecureAxis                                             |
| ntfsf.sys                        | 364700   | Sun&Moon Rise                                          |
| BssAudit.sys                     | 364600   | ByStorm                                                |
| GPMiniFIlter.sys                 | 364500   | Kalpataru                                              |
| AlfaFF.sys                       | 364400   | Alfa                                                   |
| FSAFilter.sys                    | 364300   | ScriptLogic                                            |
| GcfFilter.sys                    | 364200   | GemacmbH                                               |
| FFCFILT.SYS                      | 364100   | FFC Limited                                            |
| msnfsflt.sys                     | 364000   | Microsoft                                              |
| mblmon.sys                       | 363900   | Packeteer                                              |
| amsfilter.sys                    | 363800   | Axur Information Sec.                                  |
| strapvista.sys (retired)         | 363700   | AvSoft Technologies                                    |
| EstPrmon.sys                     | 363610   | ESTsoft corp.                                          |
| Estprp.sys - 64bit               | 363610   | ESTsoft corp.                                          |
| EstRegmon.sys                    | 363600   | ESTsoft corp.                                          |
| EstRegp.sys - 64bit              | 363600   | ESTsoft corp.                                          |
| agfsmon.sys                      | 363530   | TechnoKom Ltd.                                         |
| NlxFF.sys                        | 363520   | OnGuard Systems LLC                                    |
| Sahara.sys                       | 363511   | Safend                                                 |
| Santa.sys                        | 363510   | Safend                                                 |
| vfdrv.sys                        | 363500   | Viewfinity                                             |
| xhunter64.sys                    | 363400   | Wellbia.com                                            |
| SPIMiniFilter.sys                | 363300   | Software Pursuits                                      |
| BEDaisy.sys                      | 363220   | BattlEye Innovations                                   |
| NetAccCtrl.sys                   | 363200   | LINK co.                                               |
| NetAccCtrl64.sys                 | 363200   | LINK co.                                               |
| dsfemon.sys                      | 363100   | Topology Ltd                                           |
| iothorfs.sys                     | 363020   | ioScience                                              |
| ctamflt.sys                      | 363010   | ComTrade                                               |
| psisolator.sys                   | 363000   | SharpCrafters                                          |
| klifks.sys                       | 362902   | Kaspersky Lab                                          |
| klifaa.sys                       | 362901   | Kaspersky Lab                                          |
| Klifsm.sys                       | 362900   | Kaspersky Lab                                          |
| minispy.sys - Bottom             | 361000   | Microsoft                                              |

 

## <span id="340000_-_349999__FSFilter_Undelete"></span><span id="340000_-_349999__fsfilter_undelete"></span><span id="340000_-_349999__FSFILTER_UNDELETE"></span>340000 - 349999: FSFilter Undelete


| Minifilter       | Altitude | Company                        |
|------------------|----------|--------------------------------|
| BSSFlt.sys       | 346000   | Blue Shoe Software LLC         |
| ThinIO.sys       | 345900   | ThinScale Technology           |
| hmpalert.sys     | 345800   | SurfRight                      |
| nsffkmd64.sys    | 345700   | NetSTAR Inc.                   |
| nsffkmd32.sys    | 345700   | NetSTAR Inc.                   |
| xbprocfilter.sys | 345600   | Zrxb                           |
| ifileguard.sys   | 345500   | I-O DATA DEVICE, INC.          |
| undelex32.sys    | 345400   | Resplendence Software Projects |
| undelex64.sys    | 345400   | Resplendence Software Projects |
| starmon.sys      | 345300   | Kantowitz Engineering, Inc.    |
| mxRCycle.sys     | 345200   | Avanquest                      |
| UdFilter.sys     | 345100   | Diskeeper Corporation          |
| it2prtc.sys      | 345040   | Soliton Systems K.K.           |
| SolRegFilter.sys | 345030   | Soliton Systems K.K.           |
| SolSecBr.sys     | 345020   | Soliton Systems K.K.           |
| SolFCLLi.sys     | 345010   | Soliton Systems K.K.           |
| SolFCL.sys       | 345000   | Soliton Smart Sec              |

 

## <span id="320000_-_329998__FSFilter_Anti-Virus"></span><span id="320000_-_329998__fsfilter_anti-virus"></span><span id="320000_-_329998__FSFILTER_ANTI-VIRUS"></span>320000 - 329998: FSFilter Anti-Virus


| Minifilter                       | Altitude | Company                                                   |
|----------------------------------|----------|-----------------------------------------------------------|
| reaqtor.sys                      | 329150   | ReaQta Ltd.                                               |
| SE46Filter.sys                   | 329140   | Technology Nexus AB                                       |
| FileScan.sys                     | 329130   | NPcore Ltd                                                |
| ECATDriver.sys                   | 329120   | EMC                                                       |
| pfkrnl.sys                       | 329110   | FXSEC LTD                                                 |
| epicFilter.sys                   | 329100   | Hidden Reflex                                             |
| b9kernel.sys                     | 329050   | Bit9 Inc                                                  |
| eeCtrl.sys                       | 329010   | symantec                                                  |
| eraser.sys (Retired)             | 329010   | symantec                                                  |
| SRTSP.sys,                       | 329000   | symantec                                                  |
| SRTSPIT.sys - ia64 systems       | 329000   | symantec                                                  |
| SRTSP64.SYS - x64 systems        | 329000   | symantec                                                  |
| a2ertpx86.sys                    | 328920   | Emsi Software GmbH                                        |
| a2ertpx64.sys                    | 328920   | Emsi Software GmbH                                        |
| a2gffx86.sys - x86               | 328910   | Emsi Software GmbH                                        |
| a2gffx64.sys - x64               | 328910   | Emsi Software GmbH                                        |
| a2gffi64.sys - IA64              | 328910   | Emsi Software GmbH                                        |
| a2acc.sys                        | 328900   | Emsi Software GmbH                                        |
| a2acc64.sys on x64 systems       | 328900   | Emsi Software GmbH                                        |
| si32\_file.sys                   | 328810   | Scargo Inc                                                |
| si64\_file.sys                   | 328810   | Scargo Inc                                                |
| mbam.sys                         | 328800   | Malwarebytes Corp.                                        |
| eamonm.sys                       | 328700   | ESET, spol. s r.o.                                        |
| MaxProc64.sys                    | 328620   | Max Secure Software                                       |
| MaxProtector.sys                 | 328610   | Max Secure Software                                       |
| SDActMon.sys                     | 328600   | Max Secure Software                                       |
| fileflt.sys                      | 328540   | Trend Micro Inc.                                          |
| TmEsFlt.sys                      | 328530   | Trend Micro Inc.                                          |
| tmevtmgr.sys                     | 328510   | Trend Micro Inc.                                          |
| tmpreflt.sys                     | 328500   | Trend                                                     |
| vcMFilter.sys                    | 328400   | SGRI Co., LTD.                                            |
| SAFsFilter.sys                   | 328300   | Lightspeed Systems                                        |
| vsepflt.sys                      | 328200   | VMware                                                    |
| VFileFilter.sys(renamed)         | 328200   | VMware                                                    |
| drivesentryfilterdriver2lite.sys | 328100   | DriveSentry Inc                                           |
| WdFilter.sys                     | 328010   | Microsoft                                                 |
| mpFilter.sys                     | 328000   | Microsoft                                                 |
| vrSDetri.sys                     | 327801   | ETRI                                                      |
| vrSDetrix.sys                    | 327800   | ETRI                                                      |
| AhkSvPro.sys                     | 327720   | Ahkun Co.                                                 |
| AhkUsbFW.sys                     | 327710   | Ahkun Co.                                                 |
| AhkAMFlt.sys                     | 327700   | Ahkun Co.                                                 |
| PSINPROC.SYS                     | 327620   | Panda Security                                            |
| PSINFILE.SYS                     | 327610   | Panda Security                                            |
| amfsm.sys - Windows XP/2003 x64  | 327600   | Panda Security                                            |
| amm8660.sys - Windows Vista x86  | 327600   | Panda Security                                            |
| amm6460.sys - Windows Vista x64  | 327600   | Panda Security                                            |
| BkavSdFlt.sys                    | 327540   | Bkav Corporation                                          |
| easyanticheat.sys                | 327530   | EasyAntiCheat Solutions                                   |
| 5nine.cbt.sys                    | 327520   | 5nine Software                                            |
| caavFltr.sys                     | 327510   | Computer Assoc                                            |
| ino\_fltr.sys                    | 327500   | Computer Assoc                                            |
| WCSDriver.sys                    | 327410   | White Cloud Security                                      |
| dsark.sys                        | 327402   | Qihoo 360                                                 |
| 360avflt.sys                     | 327400   | Qihoo 360                                                 |
| ANVfsm.sys                       | 327310   | Arcdo                                                     |
| CDrRSFlt.sys                     | 327300   | Arcdo                                                     |
| EPSMn.sys                        | 327200   | SGA                                                       |
| QQSysMonX64.sys                  | 327125   | Tencent                                                   |
| QQSysMon.sys                     | 327120   | Tencent                                                   |
| TSysCare.sys                     | 327110   | Shenzhen Tencent Computer Systems Company Limited         |
| TFsFlt.sys                       | 327100   | Shenzhen Tencent Computer Systems Company Limited         |
| avmf.sys                         | 327000   | Authentium                                                |
| BDFileDefend.sys                 | 326916   | Baidu (beijing)                                           |
| BDsdKit.sys                      | 326914   | Baidu online network technology (beijing)Co.              |
| bd0003.sys                       | 326912   | Baidu online network technology (beijing)Co.              |
| Bfilter.sys                      | 326910   | Baidu (Hong Kong) Limited                                 |
| NeoKerbyFilter                   | 326900   | NeoAutus                                                  |
| PLGFltr.sys                      | 326800   | Paretologic                                               |
| wrdwizscanner.sys                | 326720   | WardWiz                                                   |
| AshAvScan.sys                    | 326700   | Ashampoo GmbH & Co. KG                                    |
| csaav.sys                        | 326600   | Cisco Systems                                             |
| oavfm.sys                        | 326550   | HSM IT-Services Gmbh                                      |
| SegMD.sys                        | 326520   | Segurmatica                                               |
| SegMP.sys                        | 326510   | Segurmatica                                               |
| SegF.sys                         | 326500   | Segurmatica                                               |
| eeyehv.sys                       | 326400   | eEye Digital Security                                     |
| eeyehv64.sys                     | 326400   | eEye Digital Security                                     |
| CpAvFilter.sys                   | 326311   | CodeProof Technologies Inc                                |
| CpAvKernel.sys                   | 326310   | CodeProof Technologies Inc                                |
| NovaShield.sys                   | 326300   | Securitas Technologies,Inc.                               |
| BdFileSpy.sys                    | 326200   | BullGuard                                                 |
| npxgd.sys                        | 326160   | INCA Internet Co.                                         |
| npxgd64.sys                      | 326160   | INCA Internet Co.                                         |
| tkpl2k.sys                       | 326150   | INCA Internet Co.                                         |
| tkpl2k64.sys                     | 326150   | INCA Internet Co.                                         |
| GKFF.sys                         | 326140   | INCA Internet Co.                                         |
| GKFF64.sys                       | 326140   | INCA Internet Co.                                         |
| tkdac2k.sys                      | 326130   | INCA Internet Co.                                         |
| tkdacxp.sys                      | 326130   | INCA Internet Co.                                         |
| tkdacxp64.sys                    | 326130   | INCA Internet Co.                                         |
| tksp2k.sys                       | 326120   | INCA Internet Co.                                         |
| tkspxp.sys                       | 326120   | INCA Internet Co.                                         |
| tkspxp64.sys                     | 326120   | INCA Internet Co.                                         |
| tkfsft.sys                       | 326110   | INCA Internet Co., Ltd                                    |
| tkfsft64.sys - 64bit             | 326110   | INCA Internet Co., Ltd                                    |
| tkfsavxp.sys - 32bit             | 326100   | INCA Internet Co., Ltd                                    |
| tkfsavxp64.sys - 64bit           | 326100   | INCA Internet Co., Ltd                                    |
| SMDrvNt.sys                      | 326040   | AhnLab, Inc.                                              |
| ATamptNt.sys                     | 326030   | AhnLab, Inc.                                              |
| V3Flt2k.sys                      | 326020   | AhnLab, Inc.                                              |
| V3MifiNt.sys                     | 326010   | Ahnlab                                                    |
| V3Ift2k.sys                      | 326000   | Ahnlab                                                    |
| V3IftmNt.sys (Old name)          | 326000   | Ahnlab                                                    |
| ArfMonNt.sys                     | 325990   | Ahnlab                                                    |
| AhnRghLh.sys                     | 325980   | Ahnlab                                                    |
| AszFltNt.sys                     | 325970   | Ahnlab                                                    |
| OMFltLh.sys                      | 325960   | Ahnlab                                                    |
| V3Flu2k.sys                      | 325950   | Ahnlab                                                    |
| TfFregNt.sys                     | 325940   | AhnLab Inc.                                               |
| vcdriv.sys                       | 325820   | Greatsoft Corp.Ltd                                        |
| vcreg.sys                        | 325810   | Greatsoft Corp.Ltd                                        |
| vchle.sys                        | 325800   | Greatsoft Corp.Ltd                                        |
| NxFsMon.sys                      | 325700   | Novatix Corporation                                       |
| AntiLeakFilter.sys               | 325600   | Individual developer (Soft3304)                           |
| NanoAVMF.sys                     | 325510   | Panda Software                                            |
| shldflt.sys                      | 325500   | Panda Software                                            |
| nprosec.sys                      | 325410   | Norman ASA                                                |
| nregsec.sys                      | 325400   | Norman ASA                                                |
| issregistry.sys                  | 325300   | IBM                                                       |
| THFilter.sys                     | 325200   | Sybonic Systems Inc                                       |
| pervac.sys                       | 325100   | PerSystems SA                                             |
| avgmfx86.sys                     | 325000   | AVG Grisoft                                               |
| avgmfx64.sys                     | 325000   | AVG Grisoft                                               |
| avgmfi64.sys                     | 325000   | AVG Grisoft                                               |
| avgmfrs.sys (retired)            | 325000   | AVG Grisoft                                               |
| fortimon2.sys                    | 324920   | Fortinet Inc.                                             |
| fortirmon.sys                    | 324910   | Fortinet Inc.                                             |
| fortishield.sys                  | 324900   | Fortinet Inc.                                             |
| mscan-rt.sys                     | 324800   | SecureBrain Corporation                                   |
| mwfsmfltr.sys                    | 324420   | MicroWorld Software Services Pvt. Ltd.                    |
| gtkdrv.sys                       | 324410   | GridinSoft LLC                                            |
| GbpKm.sys                        | 324400   | GAS Tecnologia                                            |
| crnsysm.sys                      | 324310   | Coranti                                                   |
| crncache32.sys                   | 324300   | Coranti                                                   |
| crncache64.sys                   | 324300   | Coranti                                                   |
| drwebfwft.sys                    | 324210   | Doctor Web                                                |
| DwShield.sys                     | 324200   | Doctor Web                                                |
| DwShield64.sys                   | 324200   | Doctor Web                                                |
| IProtect.sys                     | 324150   | EveryZone                                                 |
| TvFiltr.sys                      | 324140   | EveryZone INC.                                            |
| TvDriver.sys                     | 324130   | EveryZone INC.                                            |
| TvSPFltr.sys                     | 324120   | EveryZone INC.                                            |
| TvPtFile.sys                     | 324110   | EveryZone INC.                                            |
| TvMFltr.sys                      | 324100   | Everyzone                                                 |
| savonaccess.sys                  | 324000   | Sophos                                                    |
| sld.sys                          | 323990   | Sophos                                                    |
| OADevice.sys                     | 323900   | Tall Emu                                                  |
| pwipf6.sys                       | 323800   | PWI, Inc.                                                 |
| EstRkmon.sys                     | 323700   | ESTsoft corp.                                             |
| EstRkr.sys - 64bit               | 323700   | ESTsoft corp.                                             |
| dwprot.sys                       | 323610   | Doctor Web                                                |
| Spiderg3.sys                     | 323600   | Doctor Web Ltd.                                           |
| STKrnl64.sys                     | 323500   | Verdasys Inc                                              |
| UFDFilter.sys                    | 323400   | Yoggie                                                    |
| SCFltr.sys                       | 323300   | SecurtiyCoverage, Inc.                                    |
| fildds.sys                       | 323200   | Filseclab                                                 |
| fsfilter.sys                     | 323100   | MastedCode Ltd                                            |
| fpav\_rtp.sys                    | 323000   | f-protect                                                 |
| cwdriver.sys                     | 322900   | Leith Bade                                                |
| AYFilter.sys                     | 322810   | ESTsoft                                                   |
| Rtw.sys                          | 322800   | ESTsoft                                                   |
| HookSys.sys                      | 322700   | Beijing Rising Information Technology Corporation Limited |
| snscore.sys                      | 322600   | S.N.Safe&Software                                         |
| ssvhook.sys                      | 322500   | SecuLution GmbH                                           |
| strapvista.sys                   | 322400   | AvSoft Technologies                                       |
| strapvista64.sys                 | 322400   | AvSoft Technologies                                       |
| sascan.sys                       | 322300   | SecureAge Technology                                      |
| savant.sys                       | 322200   | Savant Protection, Inc.                                   |
| vrSDfmx.sys                      | 322153   | HAURI                                                     |
| vrSDfmx.sys                      | 322152   | HAURI                                                     |
| vrSDam.sys                       | 322151   | HAURI                                                     |
| vrSDam.sys                       | 322150   | HAURI                                                     |
| VRAPTFLT.sys                     | 322140   | HAURI Inc.                                                |
| VrAptDef.sys                     | 322130   | HAURI                                                     |
| VrSdCore.sys                     | 322120   | HAURI                                                     |
| VrFsFtM.sys                      | 322110   | HAURI                                                     |
| VrFsFtMX.sys(AMD64)              | 322110   | HAURI                                                     |
| vradfil2.sys                     | 322100   | HAURI                                                     |
| fsgk.sys                         | 322000   | f-secure                                                  |
| bouncer.sys                      | 321950   | CoreTrace Corporation                                     |
| PCTCore64.sys                    | 321910   | PC Tools Pty. Ltd.                                        |
| PCTCore.sys (Old name)           | 321910   | PC Tools Pty. Ltd.                                        |
| ikfilesec.sys                    | 321900   | PC Tools Pty. Ltd.                                        |
| ZxFsFilt.sys                     | 321800   | Australian Projects                                       |
| antispyfilter.sys                | 321700   | C-NetMedia Inc                                            |
| PZDrvXP.sys                      | 321600   | VisionPower Co.,Ltd.                                      |
| ggc.sys                          | 321510   | Quick Heal TechnologiesPvt. Ltd.                          |
| catflt.sys                       | 321500   | Quick Heal TechnologiesPvt. Ltd.                          |
| bdsflt.sys                       | 321490   | Quick Heal Technologies Pvt. Ltd.                         |
| arwflt.sys                       | 321480   | Quick Heal Technologies Pvt. Ltd.                         |
| csagent.sys                      | 321410   | CrowdStrike Ltd.                                          |
| kmkuflt.sys                      | 321400   | Komoku Inc.                                               |
| epdrv.sys                        | 321320   | McAfee Inc.                                               |
| mfencoas.sys                     | 321310   | McAfee Inc.                                               |
| mfehidk.sys                      | 321300   | McAfee Inc.                                               |
| cmdguard.sys                     | 321200   | Comodo Group Inc.                                         |
| K7Sentry.sys                     | 321100   | K7 Computing Private Ltd.                                 |
| nsminflt.sys                     | 321050   | NHN                                                       |
| nsminflt64.sys                   | 321050   | NHN                                                       |
| nvcmflt.sys                      | 321000   | Norman                                                    |
| dgsafe.sys                       | 320950   | KINGSOFT                                                  |
| issfltr.sys                      | 320900   | ISS                                                       |
| bdsvm.sys                        | 320830   | Bitdefender                                               |
| gzflt.sys                        | 320820   | BitDefender SRL                                           |
| bddevflt.sys                     | 320812   | BitDefender SRL                                           |
| AVCKF.SYS                        | 320810   | BitDefender SRL                                           |
| bdfsfltr.sys                     | 320800   | Softwin                                                   |
| bdfm.sys                         | 320790   | Softwin                                                   |
| AVC3.SYS                         | 320780   | BitDefender SRL                                           |
| TRUFOS.SYS                       | 320770   | BitDefender SRL                                           |
| aswmonflt.sys                    | 320700   | Alwil                                                     |
| HookCentre.sys                   | 320602   | G Data                                                    |
| PktIcpt.sys                      | 320601   | G Data                                                    |
| MiniIcpt.sys                     | 320600   | G Data                                                    |
| avgntflt.sys                     | 320500   | Avira GmbH                                                |
| klbg.sys                         | 320440   | Kaspersky                                                 |
| kldback.sys                      | 320430   | Kaspersky                                                 |
| kldlinf.sys                      | 320420   | Kaspersky                                                 |
| kldtool.sys                      | 320410   | Kaspersky                                                 |
| klif.sys                         | 320401   | Kaspersky Lab                                             |
| klif.sys                         | 320400   | Kaspersky                                                 |
| avfsmn.sys                       | 320310   | Anvisoft                                                  |
| lbd.sys                          | 320300   | Lavasoft AB                                               |
| rvsmon.sys                       | 320200   | CJSC Returnil Software                                    |
| ssfmonm.sys                      | 320100   | Webroot Software, Inc.                                    |
| VirtualAgent.sys                 | 320005   | Symantec                                                  |

 

## <span id="300000_-_309998__FSFilter_Replication"></span><span id="300000_-_309998__fsfilter_replication"></span><span id="300000_-_309998__FSFILTER_REPLICATION"></span>300000 - 309998: FSFilter Replication


| Minifilter              | Altitude | Company                 |
|-------------------------|----------|-------------------------|
| IntelCAS.sys            | 309100   | Intel Corporation       |
| mvfs.sys                | 309000   | IBM Corporation         |
| fsrecord.sys            | 305000   | Microsoft               |
| ubcminifilterdriver.sys | 304100   | Ullmore Ltd.            |
| replistor.sys           | 304000   | Legato                  |
| stfsd.sys               | 303900   | Endeavors Technologies  |
| xomf.sys                | 303800   | CA (XOSOFT)             |
| nfid.sys                | 303700   | Neverfail Group Ltd     |
| sybfilter.sys           | 303600   | Sybase, Inc.            |
| rfsfilter.sys           | 303500   | Evidian                 |
| cvmfsj.sys              | 303400   | CommVault Systems, Inc. |
| iOraFilter.sys          | 303300   | Infonic plc             |
| bkbmfd32.sys (x86)      | 303200   | BakBone Software, Inc   |
| bkbmfd64.sys (x64)      | 303200   | BakBone Software, Inc   |
| mblvn.sys               | 303100   | Packeteer               |
| AV12NFNT.sys            | 303000   | AhnLab                  |
| mDP\_win\_mini.sys      | 302900   | Macro Impact            |
| ctxubs.sys              | 302800   | Citrix Systems          |
| AxFilter.sys            | 301800   | Axcient                 |
| vxfsrep.sys             | 301700   | Symantec                |
| dellcapfd.sys           | 301600   | Dell                    |
| Sptres.sys              | 301500   | Safend                  |
| OfficeBackup.sys        | 301400   | Ushus Technologies      |
| pcvnfilt.sys            | 301300   | Blue Coat               |
| repdac.sys              | 301200   | NSI                     |
| repkap.sys              | 301100   | NSI                     |
| repdrv.sys              | 301000   | NSI                     |

 

## <span id="280000_-_289998__FSFilter_Continuous_Backup"></span><span id="280000_-_289998__fsfilter_continuous_backup"></span><span id="280000_-_289998__FSFILTER_CONTINUOUS_BACKUP"></span>280000 - 289998: FSFilter Continuous Backup


| Minifilter             | Altitude | Company               |
|------------------------|----------|-----------------------|
| Klcdp.sys              | 288900   | Kaspersky Lab         |
| splitinfmon.sys        | 288800   | Split Infinity        |
| versamatic.sys         | 288700   | Acertant Tech         |
| Yfilemon.sys           | 288690   | Yarisoft              |
| ibac.sys               | 288600   | Idealstor, LLC.       |
| fkdriver.sys           | 288500   | Filekeeper            |
| AAFileFilter.sys       | 288300   | Dell                  |
| hyperoo.sys            | 288400   | Hyperoo Ltd           |
| HyperBacCA.sys         | 285000   | Red Gate Software Ltd |
| ZMSFsFltr.sys          | 284400   | Zenith InfoTech       |
| AlfaSC.sys             | 284300   | Alfa Corporation      |
| hie\_ifs.sys           | 284200   | Hie Electronics, Inc. |
| AAFs.sys               | 284100   | AppAssure Software    |
| defilter.sys (old)     | 284000   | Microsoft             |
| tilana.sys             | 283000   | Tilana Sys            |
| VmDPFilter.sys         | 282900   | Macro Impact          |
| LbFilter.sys           | 281700   | Linkverse S.r.l.      |
| fbsfd.sys              | 281600   | Ferro Software        |
| dupleemf.sys           | 281500   | Duplee SPI, S.L.      |
| file\_tracker.sys      | 281420   | Acronis               |
| exbackup.sys           | 281410   | Acronis               |
| afcdp.sys              | 281400   | Acronis, Inc.         |
| dcefltr.sys            | 281300   | Cofio Software Ltd    |
| ipmrsync\_mfilter.sys  | 281200   | OpenMars Enterprises  |
| cascade.sys            | 281100   | JP Software           |
| filearchive.sys        | 281000   | Code Mortem           |
| syscdp.sys             | 280900   | System OK AB          |
| dpnedriver.sys (x86)   | 280850   | HP                    |
| dpnedriver64.sys (x64) | 280850   | HP                    |
| hpchgflt.sys           | 280800   | HP                    |
| VirtFile.sys           | 280700   | Symantec              |
| DeqoCPS.sys            | 280600   | Deqo                  |
| LV\_Tracker.sys        | 280500   | LiveVault             |
| tdmonxp.sys            | 280400   | TimeData              |
| nvfr\_cpd              | 280310   | Bakbone Software      |
| nvfr\_fdd              | 280300   | Bakbone Software      |
| Sptbkp.sys             | 280290   | Safend                |

 

## <span id="260000_-_269998__FSFilter_Content_Screener"></span><span id="260000_-_269998__fsfilter_content_screener"></span><span id="260000_-_269998__FSFILTER_CONTENT_SCREENER"></span>260000 - 269998: FSFilter Content Screener


| Minifilter                  | Altitude | Company                                  |
|-----------------------------|----------|------------------------------------------|
| Klshadow.sys                | 268300   | Kaspersky Lab                            |
| AliFileMonitorDriver.sys    | 268220   | Alibaba                                  |
| writeGuard.sys              | 268210   | TCXA Ltd.                                |
| KKUDKProtectKer.sys         | 268200   | Goldmessage technology co.               |
| sdfilter.sys                | 268130   | Igor Zorkov                              |
| Safe.sys                    | 268120   | rian@alum.mit.edu                        |
| mydlpdelete-scanner.sys     | 268110   | Medra Teknoloji                          |
| mydlpscanner.sys            | 268100   | Medra Teknoloji                          |
| sbapifs.sys                 | 268000   | Sunbelt Software                         |
| IccFilter.sys               | 267900   | NEC System Technologies                  |
| tflbc.sys                   | 267800   | Tani Electronics Corporation             |
| WBDrv.sys                   | 266700   | Axiana LLC                               |
| DMSamFilter.sys             | 266600   | Digimarc Corp.                           |
| 5nine.cbt.sys               | 266100   | 5nine Software                           |
| bsfs.sys                    | 266000   | Quick Heal TechnologiesPvt. Ltd.         |
| XXSFilter.sys               | 265900   | Zhe Jiang Xinxin Software Tech.          |
| AloahaUSBBlocker.sys        | 265800   | Wrocklage Intermedia                     |
| frxdrv.sys                  | 265700   | FSLogix                                  |
| FolderSecure.sys            | 265600   | Max Secure Software                      |
| XendowFLTC.sys              | 265570   | Credant Technologies                     |
| RepDac                      | 265500   | Vision Solutions                         |
| tbbdriver.sys               | 265400   | Tedesi                                   |
| spcgrd.sys                  | 265300   | FUJITSU BROAD SOLUTION                   |
| fdtlock.sys                 | 265250   | FUJITSU BROAD SOLUTION & CONSULTING Inc. |
| ssfFSC.sys                  | 265200   | SECUWARE S.L.                            |
| activ.sys                   | 265100   | Rapidware Pty Ltd                        |
| avscan.sys                  | 265010   | Microsoft                                |
| scanner.sys                 | 265000   | Microsoft                                |
| DI\_fs.sys                  | 264910   | Soft-SB                                  |
| wgnpos.sys                  | 264900   | Orchestria                               |
| odfltr.sys                  | 264810   | NetClean Technologies                    |
| ncpafltr.sys                | 264800   | NetClean Technologies                    |
| ct.sys                      | 264700   | Haute Secure                             |
| fvefsmf.sys                 | 264600   | Fortisphere, Inc.                        |
| block.sys                   | 264500   | Autonomy Systems Limited                 |
| csascr.sys                  | 264400   | Cisco Systems                            |
| SymAFR.sys                  | 264300   | Symantec Corporation                     |
| cwnep.sys                   | 264200   | Websense Inc.                            |
| spywareremover.sys          | 264150   | C-Netmedia                               |
| malwarebot.sys              | 264140   | C-Netmedia                               |
| antispywarebot.sys          | 264130   | 2Squared Inc.                            |
| adwarebot.sys               | 264120   | AntiSpyware LLC                          |
| antispyware.sys             | 264110   | AntiSpyware LLC                          |
| spywarebot.sys              | 264100   | C-Netmedia                               |
| nomp3.sys                   | 264000   | Hamish Speirs (private developer)        |
| dlfilter.sys                | 263900   | Starfield Software                       |
| sifsp.sys                   | 263800   | Secure Islands Technologies LTD          |
| DLFsFlt.sys                 | 263700   | CenterTools Software GmbH                |
| SamKeng.sys                 | 263600   | Syvik Co, Ltd.                           |
| rml.sys                     | 263500   | Logis IT Service Gmbh                    |
| vfsmfd.sys                  | 263410   | Vontu Inc.                               |
| vfsmfd.sys                  | 263400   | Vontu Inc.                               |
| acfilter.sys                | 263300   | Avalere, Inc.                            |
| psecfilter.sys              | 263200   | MDI Laboratory, Inc.                     |
| SolRedirect.sys             | 263110   | Soliton Systems                          |
| solitkm.sys                 | 263100   | Soliton Systems                          |
| ipcfs.sys                   | 263000   | NetVeda                                  |
| netgateav\_access.sys       | 262910   | NETGATE Tech. s.r.o.                     |
| spyemrg\_access.sys         | 262900   | NETGATE Tech. s.r.o.                     |
| pxrmcet.sys                 | 262800   | Proxure Inc.                             |
| EgisTecFF.sys               | 262700   | Egis Technology Inc.                     |
| fgcpac.sys                  | 262600   | Fortres Grand Corp.                      |
| saappctl.sys                | 262510   | SecureAge Technology                     |
| sadlp.sys                   | 262500   | SecureAge Technology                     |
| PEG2.sys                    | 262400   | PE GUARD                                 |
| AdminRunFlt.sys             | 262300   | Simon Jarvis                             |
| wvscr.sys                   | 262200   | Chengdu Wei Tech Inc.                    |
| psepfilter.sys              | 262100   | Absolute Software                        |
| SAMDriver.sys               | 262000   | Summit IT                                |
| nxrmflt.sys                 | 261680   | NextLabs, Inc.                           |
| hdlpflt.sys                 | 261200   | McAfee Inc.                              |
| CCFFilter.sys               | 261160   | Microsoft                                |
| cbafilt.sys                 | 261150   | Microsoft                                |
| SmbBandwidthLimitFilter.sys | 261110   | Microsoft                                |
| DfsrRo.sys                  | 261100   | Microsoft                                |
| DataScrn.sys                | 261000   | Microsoft                                |
| ldusbro.sys                 | 260900   | LANDesk Inc.                             |
| FileScreenFilter.sys        | 260800   | Veritas                                  |
| psmmfilter.sys              | 260700   | PolyServe                                |
| pctefa.sys                  | 260650   | PC Tools Pty. Ltd.                       |
| pctefa64.sys                | 260650   | PC Tools Pty. Ltd.                       |
| symefasi.sys                | 260610   | Symantec Corporation                     |
| symefa.sys                  | 260600   | Symantec                                 |
| symefa64.sys                | 260600   | Symantec                                 |
| aictracedrv\_cs.sys         | 260500   | AI Consulting                            |
| DWFIxxxx.sys                | 260410   | SciencePark Corporation                  |
| DWFIxxxx.sys                | 260400   | SciencePark Corporation                  |
| iqpk.sys                    | 260300   | Secure Islands Technologies LTD          |
| VHDFlt.sys                  | 260240   | Dell                                     |
| VHDFlt.sys                  | 260230   | Dell                                     |
| VHDFlt.sys                  | 260220   | Dell                                     |
| VHDFlt.sys                  | 260210   | Dell                                     |

 

## <span id="240000_-_249999__FSFilter_Quota_Management"></span><span id="240000_-_249999__fsfilter_quota_management"></span><span id="240000_-_249999__FSFILTER_QUOTA_MANAGEMENT"></span>240000 - 249999: FSFilter Quota Management


| Minifilter      | Altitude | Company      |
|-----------------|----------|--------------|
| ntps\_qfs.sys   | 245100   | NTP Software |
| PSSFsFilter.sys | 245000   | PSS Systems  |
| Sptqmg.sys      | 245300   | Safend       |
| storqosflt.sys  | 244000   | Microsoft    |

 

## <span id="220000_-_229999__FSFilter_System_Recovery"></span><span id="220000_-_229999__fsfilter_system_recovery"></span><span id="220000_-_229999__FSFILTER_SYSTEM_RECOVERY"></span>220000 - 229999: FSFilter System Recovery


| Minifilter   | Altitude | Company            |
|--------------|----------|--------------------|
| fbwf.sys     | 226000   | Microsoft          |
| Klsysrec.sys | 221500   | Kaspersky Lab      |
| SFDRV.SYS    | 221400   | Utixo LLC          |
| sp\_prot.sys | 221300   | Xacti Corporation  |
| nsfilep.sys  | 221200   | Netsupport Limited |
| syscow.sys   | 221100   | System OK AB       |
| fsredir.sys  | 221000   | Microsoft          |

 

## <span id="200000_-_209999__FSFilter_Cluster_File_System"></span><span id="200000_-_209999__fsfilter_cluster_file_system"></span><span id="200000_-_209999__FSFILTER_CLUSTER_FILE_SYSTEM"></span>200000 - 209999: FSFilter Cluster File System


| Minifilter          | Altitude | Company   |
|---------------------|----------|-----------|
| ResumeKeyFilter.sys | 202000   | Microsoft |

 

## <span id="180000_-_189999__FSFilter_HSM"></span><span id="180000_-_189999__fsfilter_hsm"></span><span id="180000_-_189999__FSFILTER_HSM"></span>180000 - 189999: FSFilter HSM


| Minifilter                    | Altitude | Company                         |
|-------------------------------|----------|---------------------------------|
| wcifs.sys                     | 189900   | Microsoft                       |
| quaddrasi.sys                 | 186400   | Quaddra Software                |
| gdrive.sys                    | 186300   | Google                          |
| EaseTag.sys                   | 186200   | EaseVault Technologies Inc.     |
| hcminifilter.sys              | 186100   | Happy Cloud                     |
| PDFsFilter.sys                | 186000   | Raxco Sfotware                  |
| camino.sys                    | 185900   | CaminoSoft Corp                 |
| C2C\_AF1R.SYS                 | 185810   | C2C Systems                     |
| DFdriver.sys                  | 185800   | DataFirst Corporation           |
| amfadrv.sys                   | 185700   | Quest Software Inc.             |
| HSMdriver.sys                 | 185600   | Wim Vervoorn                    |
| htdafd.sys                    | 185500   | Bridgehead Soft                 |
| SymHsm.sys                    | 185400   | Symantec                        |
| evmf.sys                      | 185100   | Symantec                        |
| otfilter.sys                  | 185000   | Overtone Soft                   |
| ithsmdrv.sys                  | 184900   | IBM                             |
| MfaFilter.sys                 | 184800   | Waterford Technologies          |
| SonyHsmMinifilter.sys         | 184700   | Sony Corporation                |
| acahsm.sys                    | 184600   | Autonomy Corporation            |
| zlhsm.sys                     | 184500   | ZL Technologies                 |
| Accesstracker.sys             | 183002   | Microsoft                       |
| Changetracker.sys             | 183001   | Microsoft                       |
| Fstier.sys                    | 183000   | Microsoft                       |
| hsmcdpflt.sys                 | 182700   | Metalogix                       |
| archivmgr.sys                 | 182690   | Metalogix                       |
| ntps\_oddm.sys                | 182600   | NTP Software                    |
| XDFileSys.sys                 | 182500   | XenData Limited                 |
| upmjit.sys                    | 182400   | Citrix Systems                  |
| AtmosFS.sys                   | 182310   | EMC Corporation                 |
| DxSpy.sys                     | 182300   | EMC Software Inc.               |
| car\_hsmflt.sys               | 182200   | Caringo, Inc.                   |
| BRDriver.sys                  | 182100   | BitRaider                       |
| BRDriver64.sys                | 182100   | BitRaider                       |
| autnhsm.sys                   | 182000   | Autonomy Corporation            |
| cthsmflt.sys                  | 181970   | ComTrade                        |
| NxMini.sys                    | 181900   | NEXSAN                          |
| npfdaflt.sys                  | 181800   | Mimosa Systems Inc              |
| AppStream.sys                 | 181700   | AppStream, Inc.                 |
| HPArcHsmX64.sys               | 181610   | Hewlett-Packard, Co.            |
| hphsmflt.sys                  | 181600   | Hewlett-Packard, Co.            |
| RepHsm.sys                    | 181500   | Double-Take Software, Inc.      |
| RepSIS.sys                    | 181490   | Double-Take Software            |
| SquashCompressionFsFilter.sys | 181410   | Squash Compression              |
| GXHSM.sys                     | 181400   | Commvault Systems, Inc          |
| EdsiHsm.sys                   | 181300   | Enterprise Data Solutions, Inc. |
| BkfMap.sys                    | 181200   | Data Storage Group              |
| hsmfilter.sys                 | 181100   | GRAU Data Storage AG            |
| mwi\_dmflt.sys                | 181000   | Moonwalk Univ                   |
| sdrefltr.sys                  | 180950   | Hitachi Data Systems            |
| fltasm.sys                    | 180900   | Global 360                      |
| cnet\_hsm.sys                 | 180850   | Carroll-Net                     |
| pntvolflt.sys                 | 180800   | PoINT Software&Systems          |
| appxstrm.sys                  | 180710   | Microsoft                       |
| wimmount.sys                  | 180700   | Microsoft                       |
| dfmflt.sys                    | 180611   | Microsoft                       |
| hsmflt.sys                    | 180600   | Microsoft                       |
| dfsrflt.sys                   | 180500   | Microsoft                       |
| dedup.sys                     | 180450   | Microsoft                       |
| sis.sys                       | 180400   | Microsoft                       |
| rbt\_wfd.sys                  | 180300   | Riverbed Technology,Inc         |

 

## <span id="170000_-_174999___FSFilter_Imaging__ex__.ZIP_"></span><span id="170000_-_174999___fsfilter_imaging__ex__.zip_"></span><span id="170000_-_174999___FSFILTER_IMAGING__EX__.ZIP_"></span>170000 - 174999: \*FSFilter Imaging (ex: .ZIP)


| Minifilter        | Altitude | Company   |
|-------------------|----------|-----------|
| virtual\_file.sys | 172000   | Acronis   |
| wimFltr.sys       | 170500   | Microsoft |

 

## <span id="160000_-_169999__FSFilter_Compression"></span><span id="160000_-_169999__fsfilter_compression"></span><span id="160000_-_169999__FSFILTER_COMPRESSION"></span>160000 - 169999: FSFilter Compression


| Minifilter        | Altitude | Company              |
|-------------------|----------|----------------------|
| CmgFFC.sys        | 166000   | Credant Technologies |
| compress.sys      | 165000   | Microsoft            |
| cmpflt.sys        | 162000   | Microsoft            |
| IridiumIO.sys     | 161700   | Confio               |
| logcompressor.sys | 161600   | VelociSQL            |
| GcfFilter.sys     | 161500   | GemacmbH             |
| ssddoubler.sys    | 161400   | Sinan Karaca         |
| Sptcmp.sys        | 161300   | Safend               |
| wimfsf.sys        | 161000   | Microsoft            |
| GEFCMP.sys        | 160100   | Symantec             |

 

## <span id="140000_-_149999__FSFilter_Encryption"></span><span id="140000_-_149999__fsfilter_encryption"></span><span id="140000_-_149999__FSFILTER_ENCRYPTION"></span>140000 - 149999: FSFilter Encryption


| Minifilter                  | Altitude | Company                               |
|-----------------------------|----------|---------------------------------------|
| EasyKryptMF.sys             | 149000   | SoftKrypt LLC                         |
| padlock.sys                 | 148910   | IntSoft Inc.                          |
| ffecore.sys                 | 148900   | Winmagic                              |
| klvfs.sys                   | 148810   | Kaspersky Lab                         |
| Klfle.sys                   | 148800   | Kaspersky Lab                         |
| ISIRM.sys                   | 148700   | ALPS SYSTEM INTERGRATION CO.          |
| bfusbenc.sys                | 148620   | bitFence Inc.                         |
| sztgbfsf.sys                | 148610   | SaferZone Co.                         |
| mwIPSDFilter.sys            | 148600   | Egis Technology Inc.                  |
| csccvdrv.sys                | 148500   | Computer Sciences Corporation         |
| aefs.sys                    | 148400   | Angelltech Corporation Xi'an          |
| IWCSEFlt.sys                | 148300   | InfoWatch                             |
| GDDmk.sys                   | 148250   | G Data Software AG                    |
| clcxcore.sys                | 148210   | AFORE Solutions Inc.                  |
| OrisLPDrv.sys               | 148200   | CGS Publishing Tech                   |
| nlemsys.sys                 | 148100   | NETLIB                                |
| prvflder.sys                | 148000   | Microsoft                             |
| ssefs.sys                   | 147900   | SecuLution GmbH                       |
| SePSed.sys                  | 147800   | Humming Heads, Inc.                   |
| dlmfencx.sys                | 147700   | Data Encryption Ltd                   |
| bbfsflt.sys                 | 147600   | Bloombase                             |
| qx10efs.sys                 | 147500   | Quixxant                              |
| MEfefs.sys                  | 147400   | Eruces Inc.                           |
| medlpflt.sys                | 147310   | Check Point Software Technologies Ltd |
| dsfa.sys                    | 147308   | Check Point Software Technologies Ltd |
| Snicrpt.sys                 | 147300   | Systemneeds, Inc                      |
| iCrypt.sys                  | 147200   | I-O DATA DEVICE, INC.                 |
| xdrmflt.sys                 | 147100   | bluefinsystems                        |
| dyFsFilter.sys              | 147000   | Scrypto Media                         |
| thinairwin.sys              | 146960   | Thin Air Inc"                         |
| UcaDataMgr.sys              | 146950   | AppSense Ltd                          |
| zesocc.sys                  | 146900   | Novell                                |
| mfprom.sys                  | 146800   | McAfee Inc                            |
| MfeEEFF.sys                 | 146790   | McAfee                                |
| intefs.sys                  | 146700   | TianYu Software                       |
| leofs.sys                   | 146600   | Leotech                               |
| autocryptater.sys           | 146500   | Richard Hagen                         |
| WavxDMgr.sys                | 146400   | Scott Cochrane                        |
| eedmkxp32.sys               | 146300   | Entrust                               |
| SbCe.sys                    | 146200   | SafeBoot                              |
| iSharedFsFilter             | 146100   | Packeteer Inc                         |
| dlmfenc.sys                 | 146000   | DESlock+                              |
| aksdf.sys                   | 145900   | Aladdin Knowledge Systems             |
| DDSFilter.sys               | 145800   | WuHan Forworld Software               |
| SecureShield.sys            | 145700   | HMI                                   |
| AifaFE.sys                  | 145600   | Alfa                                  |
| GBFsMf.sys                  | 145500   | GreenBorder                           |
| jmefs.sys                   | 145400   | ShangHai Elec                         |
| VFDriver.sys                | 145300   | R Systems                             |
| AisLeg.sys                  | 145210   | Assured Information Security          |
| windtalk.sys                | 145200   | Hyland Software                       |
| TeamCryptor.sys             | 145190   | iTwin Pte. Ltd.                       |
| CVDLP.sys                   | 145180   | CommVault Systems, Inc.               |
| 5nine.encryptor.sys         | 145170   | 5nine Software                        |
| ctpfile.sys                 | 145160   | Beijing Wondersoft Technology Co.     |
| DPDrv.sys                   | 145150   | IBM Japan                             |
| tsdlp.sys                   | 145140   | Forware                               |
| KCDriver.sys                | 145130   | Tallegra Ltd                          |
| CmgFFE.sys                  | 145120   | Credant Technologies                  |
| fgcenc.sys                  | 145110   | Fortres Grand Corp.                   |
| sview.sys                   | 145100   | Cinea                                 |
| stocc.sys                   | 145000   | Senforce Technologies                 |
| SnEfs.sys                   | 144900   | Informzaschita                        |
| ewSecureDox                 | 144800   | Echoworx Corporation                  |
| osrdmk.sys                  | 144700   | OSR Open Systems Resources, Inc.      |
| uldcr.sys                   | 144600   | NCR Financial Solutions               |
| Tkefsxp.sys - 32bit         | 144500   | INCA Internet Co., Ltd                |
| Tkefsxp64.sys - 64bit       | 144500   | INCA Internet Co., Ltd                |
| NmlAccf.sys                 | 144400   | NEC System Technologies, Ltd.         |
| SolCrypt.sys                | 144300   | Soliton Systems K.K.                  |
| IngDmk.sys                  | 144200   | Ingrian Networks, Inc.                |
| llenc.sys                   | 144100   | SecureAxis Software                   |
| SecureData.sys              | 144030   | SecureAge Technology                  |
| lockcube.sys                | 144020   | SecureAge Technology Pte Ltd          |
| sdmedia.sys                 | 144010   | SecureAge Technology                  |
| mysdrive.sys                | 144000   | SecureAge Technology                  |
| FileArmor.sys               | 143900   | Mobile Armor                          |
| VSTXEncr.sys                | 143800   | VIA Technologies, Inc.                |
| dgdmk.sys                   | 143700   | Verdasys Inc.                         |
| shandy.sys                  | 143600   | Safend Ltd.                           |
| C2knet.sys                  | 143520   | Secuware                              |
| C2kdef.sys                  | 143510   | Secuware                              |
| ssfFS.sys                   | 143500   | SECUWARE S.L.                         |
| PISRFE.sys                  | 143400   | Jilin University IT Co.               |
| bapfecre.sys                | 143300   | BitArmor Systems, Inc                 |
| KPSD.sys                    | 143200   | cihosoft                              |
| Fcfileio.sys                | 143100   | Brainzsquare, Co. Ltd.                |
| cpdrm.sys                   | 143000   | Pikewerks                             |
| vmfiltr.sys                 | 142900   | Vormetric Inc                         |
| pgpfs.sys                   | 142810   | Symantec                              |
| fencry.sys                  | 142800   | Symantec                              |
| TmFileEncDmk.sys            | 142700   | Trend Micro Inc                       |
| cpefs.sys                   | 142600   | Crypto-Pro                            |
| dekfs.sys                   | 142500   | KasherLab co.,ltd                     |
| qlockfilter.sys             | 142400   | Binqsoft Inc.                         |
| RRFilterDriverStack\_d3.sys | 142300   | Rational Retention                    |
| cve.sys                     | 142200   | Absolute Software Corp.               |
| spcflt.sys                  | 142100   | FUJITSU BSC Inc.                      |
| ldsecusb.sys                | 142000   | LANDesk Inc.                          |
| fencr.sys                   | 141900   | SODATSW spol. s.r.o.                  |
| RubiFlt.sys                 | 141800   | Hitachi                               |
| CovertxFilter.sys           | 141700   | Covertix                              |
| xbdocfilter.sys             | 141610   | Zrxb                                  |
| EVSDecrypt32.sys            | 141600   | Fortium Technologies Ltd              |
| EVSDecrypt64.sys            | 141600   | Fortium Technologies Ltd              |
| EVSDecryptia64.sys          | 141600   | Fortium Technologies Ltd              |
| afdriver.sys                | 141500   | ATUS Technology LLC                   |
| CmdMnEfs.sys                | 141420   | Comodo Security                       |
| DWENxxxx.sys                | 141410   | SciencePark Corporation               |
| DWENxxxx.sys                | 141400   | SciencePark Corporation               |
| hdFileSentryDrv32.sys       | 141300   | Heilig Defense                        |
| hdFileSentryDrv64.sys       | 141300   | Heilig Defense                        |
| Filecrypt.sys               | 141100   | Microsoft                             |
| encrypt.sys                 | 141010   | Microsoft                             |
| swapBuffers.sys             | 141000   | Microsoft                             |

 

## <span id="130000_-_139999__FSFilter_Virtualization"></span><span id="130000_-_139999__fsfilter_virtualization"></span><span id="130000_-_139999__FSFILTER_VIRTUALIZATION"></span>130000 - 139999: FSFilter Virtualization


| Minifilter             | Altitude | Company                       |
|------------------------|----------|-------------------------------|
| Klvirt.sys             | 138100   | Kaspersky Lab                 |
| rqtNos.sys             | 138030   | ReaQta Ltd.                   |
| HIPS64.sys             | 138020   | Recrypt LLC                   |
| frxdrv.sys             | 138010   | FSLogix                       |
| vzdrv.sys              | 138000   | Altiris                       |
| AppStream.sys          | 137920   | Symantec Corporation          |
| boxifier.sys           | 137910   | Kenubi                        |
| xorw.sys               | 137900   | CA (XOsoft)                   |
| ctlua.sys              | 137800   | SurfRight B.V.                |
| fgccow.sys             | 137700   | Fortres Grand Corp.           |
| aswSnx.sys             | 137600   | ALWIL Software                |
| AppIsoFltr.sys         | 137500   | Kernel Drivers                |
| ptcvfsd.sys            | 137400   | PTC                           |
| BDSandBox.sys          | 137300   | BitDefender SRL               |
| sxfpss-virt.sys        | 137200   | Skanix AS                     |
| DKRtWrt.sys            | 137100   | Diskeeper Corporation         |
| ivm.sys                | 137000   | RingCube Technologies         |
| ivm.sys                | 136990   | Citrix Systems                |
| dtiof.sys              | 136900   | Instavia Software Inc.        |
| NxTopCP.sys            | 136800   | Virtual Ccomputer Inc.        |
| svdriver.sys           | 136700   | VMware, Inc.                  |
| unifltr.sys            | 136600   | Unidesk                       |
| unidrive.sys (Renamed) | 136600   | Unidesk                       |
| ive.sys                | 136500   | TrendMicro Inc.               |
| odamf.sys              | 136450   | Sony Corporation              |
| SrMxfMf.sys            | 136440   | Sony Corporation              |
| sxsudfmf.sys           | 136410   | Sony Corporation              |
| vfammf.sys             | 136400   | Sony Corporation              |
| VHDFlt.sys             | 136240   | Dell                          |
| VHDFlt.sys             | 136230   | Dell                          |
| VHDFlt.sys             | 136220   | Dell                          |
| VHDFlt.sys             | 136210   | Dell                          |
| ncfsfltr.sys           | 136200   | NComputing                    |
| cmdguard.sys           | 136100   | COMODO Security Solutions Inc |
| svhdxflt.sys           | 135100   | Microsoft                     |
| luafv.sys              | 135000   | Microsoft                     |
| ivm.sys                | 134000   | RingCube Technologies         |
| ivm.sys                | 133990   | Citrix Systems                |
| Stcvhdmf.sys           | 132600   | StorageCraft Tech Corp        |
| appdrv01.sys           | 132500   | Protection Technology         |
| virtual\_file.sys      | 132400   | Acronis                       |
| pdiFsFilter.sys        | 132300   | Proximal Data Inc.            |
| avgvtx86.sys           | 132200   | AVG Technologies CZ           |
| avgvtx64.sys           | 132200   | AVG Technologies CZ           |
| DataNet\_Driver.sys    | 132100   | AppSense Ltd                  |
| EgenPage.sys           | 132000   | Egenera, Inc.                 |
| unidrive.sys-old       | 131900   | Unidesk                       |
| ivm.sys.old            | 131800   | RingCube Technologies         |
| XiaobaiFsR.sys         | 131710   | SHENZHEN UNNOO LTD            |
| XiaobaiFs.sys          | 131700   | SHENZHEN UNNOO LTD            |
| iotfsflt.sys           | 131600   | IO Turbine Inc                |
| mhpvfs.sys             | 131500   | Wunix Limited                 |
| svdriver.sys           | 131400   | SnapVolumes                   |
| Sptvrt.sys             | 131300   | Safend                        |
| aicvirt.sys            | 131200   | AI Consulting                 |
| sfo.sys                | 130100   | Microsoft                     |
| DeVolume.sys           | 130000   | Microsoft                     |

 

## <span id="120000_-_129999__FSFilter_Physical_Quota_Management"></span><span id="120000_-_129999__fsfilter_physical_quota_management"></span><span id="120000_-_129999__FSFILTER_PHYSICAL_QUOTA_MANAGEMENT"></span>120000 - 129999: FSFilter Physical Quota Management


| Minifilter   | Altitude | Company       |
|--------------|----------|---------------|
| quota.sys    | 125000   | Microsoft     |
| qafilter.sys | 124000   | Veritas       |
| DroboFlt.sys | 123900   | Data Robotics |

 

## <span id="100000_-_109999__FSFilter_Filter_Open_File"></span><span id="100000_-_109999__fsfilter_filter_open_file"></span><span id="100000_-_109999__FSFILTER_FILTER_OPEN_FILE"></span>100000 - 109999: FSFilter Filter Open File


| Minifilter      | Altitude | Company          |
|-----------------|----------|------------------|
| Klbackupflt.sys | 100800   | Kaspersky        |
| insyncmf.sys    | 105000   | InSync           |
| repkap          | 100700   | Vision Solutions |
| symrg.sys       | 100600   | Symantec         |
| adsfilter.sys   | 100500   | PolyServ         |

 

## <span id="80000_-_89999__FSFilter_Security_Enhancer"></span><span id="80000_-_89999__fsfilter_security_enhancer"></span><span id="80000_-_89999__FSFILTER_SECURITY_ENHANCER"></span>80000 - 89999: FSFilter Security Enhancer


<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Minifilter</th>
<th align="left">Altitude</th>
<th align="left">Company</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left">MyDLPMF.sys</td>
<td align="left">87600</td>
<td align="left">Comodo Group Inc.</td>
</tr>
<tr class="even">
<td align="left">ScuaRaw.sys</td>
<td align="left">87500</td>
<td align="left">SCUA Seguran�a da Informa�ao</td>
</tr>
<tr class="odd">
<td align="left">HDSFilter.sys</td>
<td align="left">87400</td>
<td align="left">NeoAutus Automation System</td>
</tr>
<tr class="even">
<td align="left">ikfsmflt.sys</td>
<td align="left">87300</td>
<td align="left">IronKey Inc.</td>
</tr>
<tr class="odd">
<td align="left">Klsec.sys</td>
<td align="left">87200</td>
<td align="left">Kaspersky Lab</td>
</tr>
<tr class="even">
<td align="left">XtimUSBFsFilterDrv.sys</td>
<td align="left">87190</td>
<td align="left">Dalian CP-SDT Ltd</td>
</tr>
<tr class="odd">
<td align="left">RGFLT_FM.sys</td>
<td align="left">87180</td>
<td align="left">Trusted Systems</td>
</tr>
<tr class="even">
<td align="left">flockflt.sys</td>
<td align="left">87170</td>
<td align="left">Ahranta</td>
</tr>
<tr class="odd">
<td align="left">ZdCore.sys</td>
<td align="left">87160</td>
<td align="left">Zends Technological Solutions</td>
</tr>
<tr class="even">
<td align="left">dcrypt.sys</td>
<td align="left">87150</td>
<td align="left">ReactOS Foundation</td>
</tr>
<tr class="odd">
<td align="left">hpradeo.sys</td>
<td align="left">87140</td>
<td align="left">Pradeo</td>
</tr>
<tr class="even">
<td align="left">SDFSAGDRV.SYS</td>
<td align="left">87130</td>
<td align="left">ALPS SYSTEM INTERGRATION CO.</td>
</tr>
<tr class="odd">
<td align="left">SDFSDEVFDRV.SYS</td>
<td align="left">87120</td>
<td align="left">ALPS SYSTEM INTERGRATION CO.</td>
</tr>
<tr class="even">
<td align="left">SDIFSFDRV.SYS</td>
<td align="left">87110</td>
<td align="left">ALPS SYSTEM INTERGRATION CO.</td>
</tr>
<tr class="odd">
<td align="left">SDFSFDRV.SYS</td>
<td align="left">87100</td>
<td align="left">ALPS SYSTEM INTERGRATION CO.</td>
</tr>
<tr class="even">
<td align="left">HHVolFltr.sys</td>
<td align="left">87000</td>
<td align="left">H+H Software GmbH</td>
</tr>
<tr class="odd">
<td align="left">SbieDrv.sys</td>
<td align="left">86900</td>
<td align="left">Sandboxie L.T.D</td>
</tr>
<tr class="even">
<td align="left">assetpro.sys</td>
<td align="left">86800</td>
<td align="left">pyaprotect.com</td>
</tr>
<tr class="odd">
<td align="left">dlp.sys</td>
<td align="left">86700</td>
<td align="left">Tellus Software AS</td>
</tr>
<tr class="even">
<td align="left">eps.sys</td>
<td align="left">86600</td>
<td align="left">Lumension Security</td>
</tr>
<tr class="odd">
<td align="left">RapportPG64.sys</td>
<td align="left">86500</td>
<td align="left">Trusteer</td>
</tr>
<tr class="even">
<td align="left">amminifilter.sys</td>
<td align="left">86400</td>
<td align="left">AppSense</td>
</tr>
<tr class="odd">
<td align="left">Sniflt.sys</td>
<td align="left">86300</td>
<td align="left">Systemneeds, Inc</td>
</tr>
<tr class="even">
<td align="left">SecFile.sys</td>
<td align="left">86200</td>
<td align="left">Secure By Design Inc.</td>
</tr>
<tr class="odd">
<td align="left">philly.sys</td>
<td align="left">86110</td>
<td align="left">triCerat, Inc.</td>
</tr>
<tr class="even">
<td align="left">reggy.sys</td>
<td align="left">86100</td>
<td align="left">triCerat, Inc.</td>
</tr>
<tr class="odd">
<td align="left">cygfilt.sys</td>
<td align="left">86000</td>
<td align="left">Livegrid Incorporated</td>
</tr>
<tr class="even">
<td align="left">prelaunch.sys</td>
<td align="left">85900</td>
<td align="left">D3L</td>
</tr>
<tr class="odd">
<td align="left">csareg.sys</td>
<td align="left">85810</td>
<td align="left">Cisco Systems</td>
</tr>
<tr class="even">
<td align="left">csaenh.sys</td>
<td align="left">85800</td>
<td align="left">Cisco Systems</td>
</tr>
<tr class="odd">
<td align="left">CIDACL.sys</td>
<td align="left">85700</td>
<td align="left">GE Aviation (Digital Systems Germantown)</td>
</tr>
<tr class="even">
<td align="left">CVDLP.sys</td>
<td align="left">85610</td>
<td align="left">CommVault Systems, Inc.</td>
</tr>
<tr class="odd">
<td align="left">QGPEFlt.sys</td>
<td align="left">85600</td>
<td align="left">Quest Software</td>
</tr>
<tr class="even">
<td align="left">Drveng.sys</td>
<td align="left">85500</td>
<td align="left">CA</td>
</tr>
<tr class="odd">
<td align="left">vracfil2.sys</td>
<td align="left">85400</td>
<td align="left">HAURI</td>
</tr>
<tr class="even">
<td align="left">TFsDisk.sys</td>
<td align="left">85300</td>
<td align="left">Teruten</td>
</tr>
<tr class="odd">
<td align="left">rcMiniDrv.sys</td>
<td align="left">85200</td>
<td align="left">REDGATE CO.,LTD.</td>
</tr>
<tr class="even">
<td align="left">SnMc5xx.sys</td>
<td align="left">85100</td>
<td align="left">Informzaschita</td>
</tr>
<tr class="odd">
<td align="left">FSPFltd.sys</td>
<td align="left">85010</td>
<td align="left">Alfa</td>
</tr>
<tr class="even">
<td align="left">AifaFFP.sys</td>
<td align="left">85000</td>
<td align="left">Alfa</td>
</tr>
<tr class="odd">
<td align="left">EsAccCtlFE.sys</td>
<td align="left">84901</td>
<td align="left">EgoSecure GmbH</td>
</tr>
<tr class="even">
<td align="left">DpAccCtl.sys</td>
<td align="left">84900</td>
<td align="left">Softbroker GmbH</td>
</tr>
<tr class="odd">
<td align="left">privman.sys</td>
<td align="left">84800</td>
<td align="left">BeyondTrust</td>
</tr>
<tr class="even">
<td align="left">eumntvol.sys</td>
<td align="left">84700</td>
<td align="left">Eugrid Inc</td>
</tr>
<tr class="odd">
<td align="left">SoloEncFilter.sys</td>
<td align="left">84600</td>
<td align="left">Soliton Systems</td>
</tr>
<tr class="even">
<td align="left">sbfilter.sys</td>
<td align="left">84500</td>
<td align="left">UC4 Sofware</td>
</tr>
<tr class="odd">
<td align="left">cposfw.sys</td>
<td align="left">84450</td>
<td align="left">Check Point Software Technologies Ltd</td>
</tr>
<tr class="even">
<td align="left">vsdatant.sys</td>
<td align="left">84400</td>
<td align="left">Zone Labs LLC</td>
</tr>
<tr class="odd">
<td align="left">SePnet.sys</td>
<td align="left">84350</td>
<td align="left">Humming Heads, Inc.</td>
</tr>
<tr class="even">
<td align="left">SePuld.sys</td>
<td align="left">84340</td>
<td align="left">Humming Heads, Inc.</td>
</tr>
<tr class="odd">
<td align="left">SePpld.sys</td>
<td align="left">84330</td>
<td align="left">Humming Heads, Inc.</td>
</tr>
<tr class="even">
<td align="left">SePfsd.sys</td>
<td align="left">84320</td>
<td align="left">Humming Heads, Inc.</td>
</tr>
<tr class="odd">
<td align="left">SePwld.sys</td>
<td align="left">84310</td>
<td align="left">Humming Heads, Inc.</td>
</tr>
<tr class="even">
<td align="left">SePprd.sys</td>
<td align="left">84300</td>
<td align="left">Humming Heads, Inc.</td>
</tr>
<tr class="odd">
<td align="left">InPFlter.sys</td>
<td align="left">84200</td>
<td align="left">Humming Heads, Inc.</td>
</tr>
<tr class="even">
<td align="left">CProCtrl.sys</td>
<td align="left">84100</td>
<td align="left">Crypto-Pro</td>
</tr>
<tr class="odd">
<td align="left">spyshelter.sys</td>
<td align="left">84000</td>
<td align="left">Datpol</td>
</tr>
<tr class="even">
<td align="left">clpinspprot.sys</td>
<td align="left">83900</td>
<td align="left">Information Technology Company Ltd.</td>
</tr>
<tr class="odd">
<td align="left">uvmfsflt.sys</td>
<td align="left">83376</td>
<td align="left">NEC Corporation</td>
</tr>
<tr class="even">
<td align="left">dguard.sys</td>
<td align="left">82300</td>
<td align="left">Dmitry Varshavsky</td>
</tr>
<tr class="odd">
<td align="left">NSUSBStorageFilter.sys</td>
<td align="left">82200</td>
<td align="left">NetSupport Ltd</td>
</tr>
<tr class="even">
<td align="left">RMSEFFMV.SYS</td>
<td align="left">82100</td>
<td align="left">CJSC Returnil Software</td>
</tr>
<tr class="odd">
<td align="left">BoksFLAC.sys</td>
<td align="left">82000</td>
<td align="left">Fox Technologies</td>
</tr>
<tr class="even">
<td align="left">cpAcOnPnP.sys</td>
<td align="left">81910</td>
<td align="left">conpal GmbH</td>
</tr>
<tr class="odd">
<td align="left">cpsgfsmf.sys</td>
<td align="left">81900</td>
<td align="left">conpal GmbH</td>
</tr>
<tr class="even">
<td align="left">ndevsec.sys</td>
<td align="left">81800</td>
<td align="left">Norman ASA</td>
</tr>
<tr class="odd">
<td align="left">ViewIntus_RTDG.sys</td>
<td align="left">81700</td>
<td align="left">Pentego Technologies Ltd</td>
</tr>
<tr class="even">
<td align="left">zam.sys</td>
<td align="left">81620</td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left">ANXfsm.sys</td>
<td align="left">81610</td>
<td align="left">Arcdo</td>
</tr>
<tr class="even">
<td align="left">CDrSDFlt.sys</td>
<td align="left">81600</td>
<td align="left">Arcdo</td>
</tr>
<tr class="odd">
<td align="left">crnselfdefence32.sys</td>
<td align="left">81500</td>
<td align="left">Coranti</td>
</tr>
<tr class="even">
<td align="left">crnselfdefence64.sys</td>
<td align="left">81500</td>
<td align="left">Coranti</td>
</tr>
<tr class="odd">
<td align="left">zlock_drv.sys</td>
<td align="left">81400</td>
<td align="left">SecurIT</td>
</tr>
<tr class="even">
<td align="left">f101fs.sys</td>
<td align="left">81300</td>
<td align="left">Fortres Grand Corp.</td>
</tr>
<tr class="odd">
<td align="left">sysgar.sys</td>
<td align="left">81200</td>
<td align="left">Nucleus Data Recover</td>
</tr>
<tr class="even">
<td align="left">EmbargoM.sys</td>
<td align="left">81100</td>
<td align="left">ScriptLogic</td>
</tr>
<tr class="odd">
<td align="left">fsds2a.sys</td>
<td align="left">81000</td>
<td align="left">Splitstreem Ltd</td>
</tr>
<tr class="even">
<td align="left">csacentr.sys</td>
<td align="left">80900</td>
<td align="left">Cisco Systems</td>
</tr>
<tr class="odd">
<td align="left">paritydriver.sys</td>
<td align="left">80800</td>
<td align="left">Bit9, Inc.</td>
</tr>
<tr class="even">
<td align="left">nkfsprot.sys</td>
<td align="left">80710</td>
<td align="left">Konneka</td>
</tr>
<tr class="odd">
<td align="left">nkprot.sys</td>
<td align="left">80700</td>
<td align="left">KONNEKA Information Technologies</td>
</tr>
<tr class="even">
<td align="left">acpadlock.sys</td>
<td align="left">80691</td>
<td align="left">IntSoft Co</td>
</tr>
<tr class="odd">
<td align="left">ksmf.sys</td>
<td align="left">80690</td>
<td align="left">IntSoft Co</td>
</tr>
<tr class="even">
<td align="left">im.sys</td>
<td align="left">80680</td>
<td align="left">CrowdStrike</td>
</tr>
</tbody>
</table>

 

## <span id="60000_-_69999__FSFilter_Copy_Protection"></span><span id="60000_-_69999__fsfilter_copy_protection"></span><span id="60000_-_69999__FSFILTER_COPY_PROTECTION"></span>60000 - 69999: FSFilter Copy Protection


| Minifilter             | Altitude | Company                                 |
|------------------------|----------|-----------------------------------------|
| CkProcess.sys          | 66100    | KASHU SYSTEM DESIGN INC.                |
| dlmfprot.sys           | 66000    | Data Encrypt Sys                        |
| baprtsef.sys           | 65700    | BitArmor Systems, Inc                   |
| sxfpss.sys             | 65600    | Skanix AS                               |
| rgasdev.sys            | 65500    | Macrovision                             |
| SkyWPDrv.sys           | 65400    | Sky Co.,Ltd.                            |
| SnEraser.sys           | 65300    | Informzaschita                          |
| vfilter.sys            | 65200    | RSJ Software GmbH                       |
| COGOFlt32.sys          | 65100    | Fortium Technologies Ltd                |
| COGOFlt64.sys          | 65100    | Fortium Technologies Ltd                |
| COGOFLTia64.sys        | 65100    | Fortium Technologies Ltd                |
| scrubber.sys           | 65000    | Microsoft                               |
| BRDriver.sys           | 64000    | BitRaider LLC                           |
| BRDriver64.sys         | 64000    | BitRaider LLC                           |
| LibertyFSF.sys         | 62300    | Bayalink Solutions Co                   |
| axfsdrv2.sys           | 62100    | Axence Software                         |
| sds.sys                | 62000    | Egress Software                         |
| TotalSystemAuditor.sys | 61600    | ANRC LLC                                |
| MBAMApiary.sys         | 61500    | Malwarebytes Corp.                      |
| WA\_FSW.sys            | 61400    | Programas Administraci�n y Mejoramiento |
| ViewIntus\_RTAS        | 61300    | Pentego Technologies                    |
| tffac.sys              | 61200    | Toshiba Corporation                     |
| tccp.sys               | 61100    | TrusCont Ltd                            |
| KomFS.sys              | 61000    | KOM Networks                            |

 

## <span id="40000_-_49999__FSFilter_Bottom"></span><span id="40000_-_49999__fsfilter_bottom"></span><span id="40000_-_49999__FSFILTER_BOTTOM"></span>40000 - 49999: FSFilter Bottom


| Minifilter         | Altitude | Company            |
|--------------------|----------|--------------------|
| aictracedrv\_b.sys | 47000    | AI Consulting      |
| hhdcfltr.sys       | 46900    | Seagate Technology |
| Npsvctrig.sys      | 46000    | Microsoft          |
| fileinfo           | 45000    | Microsoft          |
| klvfs.sys          | 44900    | Kaspersky Lab      |
| rsfxdrv.sys        | 41000    | Microsoft          |
| defilter.sys       | 40900    | Microsoft          |
| AppVVemgr.sys      | 40800    | Microsoft          |
| wof.sys            | 40700    | Microsoft          |

 

## <span id="20000_-_29999__FSFilter_System"></span><span id="20000_-_29999__fsfilter_system"></span><span id="20000_-_29999__FSFILTER_SYSTEM"></span>20000 - 29999: FSFilter System


None.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20Allocated%20Altitudes%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


