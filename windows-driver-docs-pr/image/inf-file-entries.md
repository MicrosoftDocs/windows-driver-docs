---
title: INF File Entries
author: windows-driver-content
description: INF File Entries
MS-HAID:
- 'WIA\_db\_hello\_8fcb0f6f-51d9-4bd8-b775-7dcaece8c387.xml'
- 'image.inf\_file\_entries'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 8af2cbe7-f249-4e2f-940f-b50bc451cabe
---

# INF File Entries


## <a href="" id="ddk-inf-file-entries-si"></a>


Using a microdriver for your device requires additional entries in the setup information (INF) file. First, there must be an entry called "MicroDriver" in the **DeviceData** section of the INF file. (See [INF Files for WIA Devices](inf-files-for-wia-devices.md) for more information.) This entry should be set to the name of the DLL that implements the microdriver.

### Windows Me INF File Entries

The following applies to Microsoft Windows Millennium Edition (Me), Windows XP, and later operating systems.

In the space in the [**INF AddReg Directive**](https://msdn.microsoft.com/library/windows/hardware/ff546320) where your WIA minidriver normally would be referenced, the INF should list *wiafbdrv.dll* as the driver. This is the component that implements the WIA flatbed driver.

Be sure that the [**INF CopyFiles Directive**](https://msdn.microsoft.com/library/windows/hardware/ff546346) includes both your microdriver and *wiafbdrv.dll*, which is copied from the Windows CAB files. The rest of the INF file is the same as for other WIA devices.

### Windows XP INF File Entries

The following information applies to Windows XP and later. Windows Me INF files do not use **Include** and **Needs** directives, and so cannot use this style of INF.

The [**INF DDInstall Section**](https://msdn.microsoft.com/library/windows/hardware/ff547344) should contain the directive **Include**=sti.inf. Additionally, the **Needs** directive should reference **STI.MICRODRIVERSection**, as well as the appropriate device type section. This will supply the necessary USDClass and CLSID **AddReg** directives, so these do not need to be explicitly included in the INF.

**Note**  It is not necessary to include *wiafbdrv.dll* in your **CopyFiles** directive.

 

The INF included with the WIA microdriver on the Windows Driver Kit (WDK) CD uses this new method to reference the microdriver.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20INF%20File%20Entries%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


