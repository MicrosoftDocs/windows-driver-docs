---
title: Sample INF File for a Web Services Scanner
author: windows-driver-content
description: Sample INF File for a Web Services Scanner
ms.assetid: 1e65739f-9216-4962-9108-60ba291ff052
---

# Sample INF File for a Web Services Scanner


The following INF file, *Sti.inf*, shows how to install a WIA driver. Entries that you need for *WSDScan.sys* are highlighted.

**Note**   The requirements for the device hardware IDs and the **PKEY\_Device\_HardwareIds** property that are referenced in the following INF example are described in the [PNP-X Implementer's Guide](http://go.microsoft.com/fwlink/p/?linkid=242570).

 

```
;
; MyWSScanner.inf - sample installation file that shows how
; to install a WIA driver for a WS scanner by using the inbox 
; WSDScan.sys kernel driver
;
[Version]
Signature="$WINDOWS NT$"
Class=Image
ClassGUID={6bdd1fc6-810f-11d0-bec7-08002be2092f} 
Provider=%Mfg%
DriverVer=1/17/2006,1.0.0.0 ; replace with the actual driver date 
; and version

[SourceDisksFiles.x86]
YourWIADriver.dll=1

[SourceDisksNames.x86]
1=%Location%,,,

[SourceDisksFiles.ia64]
YourWIADriver.dll=1

[SourceDisksNames.ia64]
1=%Location%,,,

[SourceDisksFiles.amd64]
YourWIADriver.dll=1

[SourceDisksNames.amd64]
1=%Location%,,,

[DestinationDirs]
DefaultDestDir = 11

[Manufacturer]
%Mfg%=Models,NTx86,NTamd64,NTia64

;
; Replace UMB\PnPX_YourDevice_HardwareID in the three Models 
; sections below to match the actual hardware IDs and compatible 
; IDs from the metadata that is supplied by the device, as it 
; is described in the PNP-X Implementer&#39;s Guide for the 
; PKEY_Device_HardwareIds property:
;

[Models.NTx86]
%WSDScanDriver.DeviceDesc% = WSDScanDriver.Device, UMB\PnPX_YourDevice_HardwareID

[Models.NTamd64]
%WSDScanDriver.DeviceDesc% = WSDScanDriver.Device, UMB\PnPX_YourDevice_HardwareID

[Models.NTia64]
%WSDScanDriver.DeviceDesc% = WSDScanDriver.Device, UMB\PnPX_YourDevice_HardwareID

[WSDScanDriver.Device]
Include=sti.inf
Needs=STI.WSDSection
SubClass=StillImage
DeviceType=1            ; scanner device
DeviceSubType=1
Capabilities=0x31       ; STI_GENCAP_NOTIFICATIONS (bit 0) | STI_GENCAP_WIA (bit 4) | bit 5
DeviceData=WSDScanDriver.DeviceData
Events=WSDScanDriver.Events
AddReg=WSDScanDriver.AddReg
CopyFiles=WSDScanDriver.CopyFiles
ICMProfiles="sRGB Color Space Profile.icm"

[WSDScanDriver.CopyFiles]
MyWIADriver.dll

;
; Do not forget to replace 00000000-0000-0000-0000-000000000000
; in the AddReg section below with the actual UUID for your WIA 
; minidriver:
;

[WSDScanDriver.AddReg]
HKR,,HardwareConfig,1,1 ; generic WDM device
HKR,,USDClass,,"{00000000-0000-0000-0000-000000000000}" 
; the GUID for the WIA mini-driver
HKCR,CLSID\{00000000-0000-0000-0000-000000000000},,,"<Description 
of your Web Services scanner WIA device>"
HKCR,CLSID\{00000000-0000-0000-0000-000000000000}\InProcServer32,,,%11%\YourWIADriver.dll
HKCR,CLSID\{00000000-0000-0000-0000-000000000000}\InProcServer32,ThreadingModel,,"Both"

[WSDScanDriver.DeviceData]
Server=local           ; the WIA mini-driver runs on the same 
machine as the client application

[WSDScanDriver.Events]
ScanEvent=%ScanEvent.Desc%,{A6C5A715-8C6E-11d2-977A-0000F87A926F},*
ScanToPrintEvent=%ScanToPrintEvent.Desc%,{B441f425-8C6e-11D2-977A-0000F87A926F},*
ScanToFaxEvent=%ScanToFaxEvent.Desc%,{C00EB793-8C6E-11D2-977A-0000F87A926F},*
ScanToOCREvent=%ScanToOCREvent.Desc%,{9D095B89-37D6-4877-AFED-62A297DC6DBE},*
ScanToEmailEvent=%ScanToEmailEvent.Desc%,{C686DCEE-54F2-419E-9A27-2FC7F2E98F9E},*

[WSDScanDriver.Device.HW]
Include=sti.inf
Needs=STI.WSDSectionHW

[WSDScanDriver.Device.Services]
Include=sti.inf
Needs=STI.WSDSection.Services

[Strings]
Mfg="<Your company name here>"
Location="<Your installation source name here>"
WSDScanDriver.DeviceDesc="<Your Web Services WIA device description>"
ScanEvent.Desc="Scan"
ScanToPrintEvent.Desc="Scan To Print"
ScanToFaxEvent.Desc="Scan To Fax"
ScanToOCREvent.Desc="Scan To OCR"
ScanToEmailEvent.Desc="Scan To E-mail"
```

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Sample%20INF%20File%20for%20a%20Web%20Services%20Scanner%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


