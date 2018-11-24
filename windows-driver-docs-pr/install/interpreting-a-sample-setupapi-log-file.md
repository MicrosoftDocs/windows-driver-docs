---
title: Interpreting a Sample SetupAPI Log File
description: Interpreting a Sample SetupAPI Log File
ms.assetid: 86bef34e-1ff3-4777-9b7c-0f08645ff89f
keywords:
- sample logs WDK SetupAPI
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Interpreting a Sample SetupAPI Log File





The sample logs below illustrate the information that is contained in a SetupAPI log file.

In general, all parts of an installation appear together in the log file. An installation section in the log starts with an entry of the format \[*year/month/day time process-id.instance description*\] where *instance* is a number that ensures that two sections instantiated at the same time for the same process are unique.

### <a href="" id="ddk-sample-windows-xp-setupapi-log-file-dg"></a>Sample Windows XP SetupAPI Log File

For Windows XP, each log entry includes a message identifier consisting of a letter or dash (-) followed by a number. The following table describes the format for message identifiers.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Message ID</th>
<th align="left">Message Type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>#E<em>nnn</em></p></td>
<td align="left"><p>Error message.</p></td>
</tr>
<tr class="even">
<td align="left"><p>#W<em>nnn</em></p></td>
<td align="left"><p>Warning message.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>#I<em>nnn</em></p></td>
<td align="left"><p>Informational message.</p></td>
</tr>
<tr class="even">
<td align="left"><p>#T<em>nnn</em></p></td>
<td align="left"><p>Timing message.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>#V<em>nnn</em></p></td>
<td align="left"><p>Verbose message.</p></td>
</tr>
<tr class="even">
<td align="left"><p>#-<em>nnn</em></p></td>
<td align="left"><p>Status message.</p></td>
</tr>
</tbody>
</table>

 

The following segments are from a Windows XP error log:

```cpp
[2001/02/27 20:14:30 1148.173]
#-198 Command line processed: C:\WINDOWS\system32\mmc.exe "C:\WINDOWS\system32\devmgmt.msc" 
#-147 Loading class installer module for "Communications Port".
@ 20:14:33.381 #V132 File "C:\WINDOWS\INF\certclas.inf" (key "certclas.inf") is signed in catalog "C:\WINDOWS\System32\CatRoot\{F750E6C3-38EE-11D1-85E5-00C04FC295EE}\NT5INF.CAT".
@ 20:14:33.810 #V132 File "C:\WINDOWS\System32\MsPorts.Dll" (key "MsPorts.Dll") is signed in catalog "C:\WINDOWS\System32\CatRoot\{F750E6C3-38EE-11D1-85E5-00C04FC295EE}\NT5.CAT".
@ 20:14:33.873 #V146 Using exported function "PortsClassInstaller" in module "C:\WINDOWS\System32\MsPorts.Dll".
@ 20:14:33.873 #V166 Device install function: DIF_UPDATEDRIVER_UI.
@ 20:14:33.873 #T152 Executing class installer.
@ 20:14:33.873 #V153 Completed class installer.
@ 20:14:33.889 #V155 Executing default installer.
@ 20:14:33.889 #V156 Completed default installer.
@ 20:14:36.302 #I060 Set selected driver.
#-019 Searching for hardware ID(s): *pnp0501
@ 20:14:36.318 #V017 Enumerating files "C:\WINDOWS\inf".
(following #V lines are logged only if driver bits of log level >= 0x7000)
@ 20:14:36.556 #V392 Using INF cache "C:\WINDOWS\inf\INFCACHE.1".
@ 20:14:36.731 #V073 Cache: Excluding INF "accessor.inf".
@ 20:14:36.731 #V073 Cache: Excluding INF "agtinst.inf".
:
:
@ 20:14:37.318 #T075 Enumerating files: Directory pass completed.
@ 20:14:37.398 #V005 Opened the PNF file of "C:\WINDOWS\inf\msports.inf" (Languge = 0409).
@ 20:14:37.413 #I022 Found "*PNP0501" in C:\WINDOWS\inf\msports.inf; Device: "Communications Port"; Driver: "Communications Port"; Provider: "Microsoft"; Mfg: "(Standard port types)"; Section name: "ComPort".
(rank of 0 is absolute best match)
@ 20:14:37.413 #I023 Actual install section: [ComPort.NT]. Rank: 0x00001000. Effective driver date: 02/14/2001.
@ 20:14:37.413 #I022 Found "*PNP0501" in C:\WINDOWS\inf\msports.inf; Device: "Communications Port"; Driver: "Communications Port"; Provider: "Microsoft"; Mfg: "(Standard port types)"; Section name: "ComPort".
@ 20:14:37.413 #I023 Actual install section: [ComPort.NT]. Rank: 0x00000000. Effective driver date: 02/14/2001.
@ 20:14:37.413 #T076 Enumerating files: Cache pass completed.
@ 20:15:01.383 #V166 Device install function: DIF_SELECTBESTCOMPATDRV.
@ 20:15:01.383 #T152 Executing class installer.
@ 20:15:01.383 #V153 Completed class installer.
@ 20:15:01.399 #V155 Executing default installer.
@ 20:15:01.399 #I063 Selected driver installs from section [ComPort] in "c:\windows\inf\msports.inf".
@ 20:15:01.526 #I320 Class GUID of device remains {4D36E978-E325-11CE-BFC1-08002BE10318}.
@ 20:15:01.526 #I060 Set selected driver.
@ 20:15:01.526 #I058 Selected best compatible driver.
@ 20:15:01.526 #V156 Completed default installer.
@ 20:15:02.447 #V166 Device install function: DIF_ALLOW_INSTALL.
@ 20:15:02.447 #T152 Executing class installer.
@ 20:15:02.447 #V153 Completed class installer.
@ 20:15:02.447 #V155 Executing default installer.
@ 20:15:02.447 #V156 Completed default installer.
@ 20:15:02.463 #V166 Device install function: DIF_INSTALLDEVICEFILES.
@ 20:15:02.463 #T152 Executing class installer.
@ 20:15:02.463 #V153 Completed class installer.
@ 20:15:02.463 #V155 Executing default installer.
@ 20:15:02.463 #T200 Install Device: Begin.
@ 20:15:02.478 #V124 Doing copy-only install of "ROOT\*PNP0501\PNPBIOS_17".
@ 20:15:02.478 #V005 Opened the PNF file of "c:\windows\inf\msports.inf" (Languge = 0409).
@ 20:15:02.478 #V005 Opened the PNF file of "c:\windows\inf\layout.inf" (Languge = 0409).
@ 20:15:02.494 #V011 Installing section [ComPort.NT] from "c:\windows\inf\msports.inf".
@ 20:15:02.494 #T203 Install Device: Queuing files from INF(s).
@ 20:15:02.510 #V005 Opened the PNF file of "C:\WINDOWS\INF\drvindex.inf" (Languge = 0409).
@ 20:15:02.590 #V094 Queued copy from section [ComPort.NT.Copy] in "c:\windows\inf\msports.inf": "serial.sys" to "serial.sys" with flags 0x80000024, target directory is "C:\WINDOWS\System32\DRIVERS".
@ 20:15:02.590 #V096 Source in section [sourcedisksfiles] in "c:\windows\inf\layout.inf"; Media=1 Description="Windows XP Professional CD-ROM" Tag="\win51ip.b2" Path="\i386". Driver cache will be used.
@ 20:15:02.605 #V132 File "C:\WINDOWS\INF\certclas.inf" (key "certclas.inf") is signed in catalog "C:\WINDOWS\System32\CatRoot\{F750E6C3-38EE-11D1-85E5-00C04FC295EE}\NT5INF.CAT".
@ 20:15:02.605 #V005 Opened the PNF file of "C:\WINDOWS\INF\certclas.inf" (Languge = 0409).
@ 20:15:02.685 #V094 Queued copy from section [ComPort.NT.Copy] in "c:\windows\inf\msports.inf": "serenum.sys" to "serenum.sys" with flags 0x80000024, target directory is "C:\WINDOWS\System32\DRIVERS".
@ 20:15:02.685 #V096 Source in section [sourcedisksfiles] in "c:\windows\inf\layout.inf"; Media=1 Description="Windows XP Professional CD-ROM" Tag="\win51ip.b2" Path="\i386". Driver cache will be used.
@ 20:15:02.685 #T204 Install Device: Queuing coinstaller files from INF(s).
@ 20:15:02.685 #V005 Opened the PNF file of "c:\windows\inf\msports.inf" (Languge = 0409).
@ 20:15:02.701 #V005 Opened the PNF file of "c:\windows\inf\layout.inf" (Languge = 0409).
#-046 Processing Coinstaller registration section [ComPort.NT.CoInstallers].
@ 20:15:02.701 #V056 Coinstallers registered.
@ 20:15:02.717 #V011 Installing section [ComPort.NT.Interfaces] from "c:\windows\inf\msports.inf".
@ 20:15:02.732 #V054 Interfaces installed.
@ 20:15:02.732 #V121 Device install of "ROOT\*PNP0501\PNPBIOS_17" finished successfully.
@ 20:15:02.732 #T201 Install Device: End.
@ 20:15:02.748 #V156 Completed default installer.
@ 20:15:02.748 #T185 Pruning Files: Verifying catalogs/infs.
@ 20:15:02.764 #V132 File "c:\windows\inf\msports.inf" (key "msports.inf") is signed in catalog "C:\WINDOWS\System32\CatRoot\{F750E6C3-38EE-11D1-85E5-00C04FC295EE}\NT5INF.CAT".
@ 20:15:02.812 #V132 File "c:\windows\inf\layout.inf" (key "layout.inf") is signed in catalog "C:\WINDOWS\System32\CatRoot\{F750E6C3-38EE-11D1-85E5-00C04FC295EE}\NT5INF.CAT".
@ 20:15:02.812 #T186 Pruning Files: Verifying catalogs/infs completed.
@ 20:15:02.859 #V132 File "C:\WINDOWS\System32\DRIVERS\serial.sys" (key "serial.sys") is signed in catalog "C:\WINDOWS\System32\CatRoot\{F750E6C3-38EE-11D1-85E5-00C04FC295EE}\NT5.CAT".
@ 20:15:02.875 #V191 File "C:\WINDOWS\System32\DRIVERS\serial.sys" pruned from copy.
@ 20:15:02.875 #V132 File "C:\WINDOWS\System32\DRIVERS\serenum.sys" (key "serenum.sys") is signed in catalog "C:\WINDOWS\System32\CatRoot\{F750E6C3-38EE-11D1-85E5-00C04FC295EE}\NT5.CAT".
@ 20:15:02.875 #V191 File "C:\WINDOWS\System32\DRIVERS\serenum.sys" pruned from copy.
@ 20:15:02.875 #V166 Device install function: DIF_REGISTER_COINSTALLERS.
@ 20:15:02.923 #T152 Executing class installer.
@ 20:15:02.939 #V153 Completed class installer.
@ 20:15:02.939 #V155 Executing default installer.
@ 20:15:02.939 #V005 Opened the PNF file of "c:\windows\inf\msports.inf" (Languge = 0409).
@ 20:15:02.939 #I056 Coinstallers registered.
@ 20:15:02.955 #V156 Completed default installer.
@ 20:15:02.955 #V166 Device install function: DIF_INSTALLINTERFACES.
@ 20:15:02.955 #T152 Executing class installer.
@ 20:15:02.955 #V153 Completed class installer.
@ 20:15:02.955 #V155 Executing default installer.
@ 20:15:02.971 #V005 Opened the PNF file of "c:\windows\inf\msports.inf" (Languge = 0409).
@ 20:15:02.971 #V011 Installing section [ComPort.NT.Interfaces] from "c:\windows\inf\msports.inf".
@ 20:15:02.986 #I054 Interfaces installed.
@ 20:15:02.986 #V156 Completed default installer.
@ 20:15:02.986 #V166 Device install function: DIF_INSTALLDEVICE.
@ 20:15:03.002 #T152 Executing class installer.
@ 20:15:03.002 #V005 Opened the PNF file of "c:\windows\inf\msports.inf" (Languge = 0409).
@ 20:15:03.018 #T200 Install Device: Begin.
@ 20:15:03.018 #I123 Doing full install of "ROOT\*PNP0501\PNPBIOS_17".
@ 20:15:03.018 #V005 Opened the PNF file of "c:\windows\inf\msports.inf" (Languge = 0409).
@ 20:15:03.018 #T211 Install Device: Changing registry settings as specified by the INF(s).
@ 20:15:03.034 #T212 Install Device: Writing driver specific registry settings.
@ 20:15:03.050 #T213 Install Device: Installing required Windows services.
#-035 Processing service Add/Delete section [ComPort.NT.Services].
@ 20:15:03.320 #V282 Add Service: Modified existing service "Serial".
@ 20:15:03.653 #V282 Add Service: Modified existing service "Serenum".
@ 20:15:03.669 #T214 Install Device: Writing drive descriptive registry settings.
@ 20:15:03.669 #T216 Install Device: Restarting device.
@ 20:15:06.399 #T217 Install Device: Restarting device completed.
@ 20:15:06.399 #W114 Device "ROOT\*PNP0501\PNPBIOS_17" required reboot: Device has problem: 0x0c: CM_PROB_NORMAL_CONFLICT.
@ 20:15:06.399 #T222 Install Device: Calling RunOnce/GrpConv items.
@ 20:15:06.415 #I138 Executing RunOnce to process 5 RunOnce entries.
@ 20:15:07.241 #I121 Device install of "ROOT\*PNP0501\PNPBIOS_17" finished successfully.
@ 20:15:07.272 #T201 Install Device: End.
@ 20:15:07.336 #V153 Completed class installer.
@ 20:15:07.368 #V166 Device install function: DIF_NEWDEVICEWIZARD_FINISHINSTALL.
@ 20:15:07.368 #T152 Executing class installer.
@ 20:15:07.495 #V153 Completed class installer.
@ 20:15:07.495 #V155 Executing default installer.
@ 20:15:07.495 #V156 Completed default installer.
@ 20:15:42.100 #V166 Device install function: DIF_DESTROYPRIVATEDATA.
@ 20:15:42.100 #T152 Executing class installer.
@ 20:15:42.100 #V153 Completed class installer.
@ 20:15:42.116 #V155 Executing default installer.
@ 20:15:42.116 #V156 Completed default installer.
```

 

 





