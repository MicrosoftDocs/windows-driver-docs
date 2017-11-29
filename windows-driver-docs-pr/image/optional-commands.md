---
title: Optional Commands
description: Optional Commands
ms.assetid: b9c411b1-0061-468a-b900-47c6062aa3b0
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Optional Commands


## <span id="ddk_optional_commands_si"></span><span id="DDK_OPTIONAL_COMMANDS_SI"></span>


The following commands can be implemented by the microdriver, but it is not required to do so.

<span id="CMD_GETSUPPORTEDFILEFORMATS"></span><span id="cmd_getsupportedfileformats"></span>CMD\_GETSUPPORTEDFILEFORMATS  
Called by the WIA Flatbed Driver to get the number of additional file formats. Two members of the passed [**VAL**](https://msdn.microsoft.com/library/windows/hardware/ff548627) structure should be filled in: **lVal** should be set to the number of additional file formats; **pGuid** should point to an array of image format GUIDs. The memory allocated for this array is owned by the microdriver and should only be freed by it.

Image formats are listed in *wiadef.h* or can be defined as custom formats. Note that because the BMP (file) and MEMORYBMP (memory) formats are required formats, the WIA Flatbed Driver automatically adds them. The microdriver should not add them to its extended list.

This command is optional unless the device can support extra file formats.

<span id="CMD_GETSUPPORTEDMEMORYFORMATS"></span><span id="cmd_getsupportedmemoryformats"></span>CMD\_GETSUPPORTEDMEMORYFORMATS  
Called by the WIA Flatbed Driver to get the number of additional memory formats. Two members of the passed [**VAL**](https://msdn.microsoft.com/library/windows/hardware/ff548627) structure should be filled in: **lVal** should be set to the number of additional memory formats; **pGuid** should point to an array of image format GUIDs. The memory allocated for this array is owned by the microdriver and should only be freed by it.

Image formats are listed in *wiadef.h* or can be defined as custom formats. Note that because the BMP (file) and MEMORYBMP (memory) formats are required formats, the WIA Flatbed Driver automatically adds them. The microdriver should not add them to its extended list.

This command is optional unless the device can support extra memory formats.

<span id="CMD_SETFORMAT"></span><span id="cmd_setformat"></span>CMD\_SETFORMAT  
The class driver sends this command to set the current format as requested by the application. The **pGuid** member of the [**VAL**](https://msdn.microsoft.com/library/windows/hardware/ff548627) structure contains the image format GUID. The microdriver should save this image format ID in its private context, in order to keep track of the current image format setting.

Microdrivers are required to support this command only if they report extended formats. Because the class driver has no way of validating data in extended formats, it is the microdriver's responsibility to generate the proper data. When transferring data in an extended format, all data should be transferred, including image headers. For example, if your driver reports that it supports the JPEG format, then all of the JPEG must be transferred, not just the image bits.

The class driver owns the memory pointed to by the **pGuid** member of the VAL structure, so the microdriver must not free it.

Note that this command does not affect the way a microdriver responds to calls to its [**Scan**](https://msdn.microsoft.com/library/windows/hardware/ff547322) function. As usual, the microdriver must check the values of the *lPhase*, *pScanInfo*, and *lLength* parameters of this function, and place data in the buffers pointed to by the *pBuffer* and *pReceived* parameters as appropriate.

Drivers that support only files in the WiaImgFmt\_BMP and WiaImgFmt\_MEMORYBMP formats (the default formats for microdrivers) can receive the CMD\_SETFORMAT command. These drivers can ignore this command, because the class driver handles all data transfers using the default formats.

<span id="CMD_SETSCANMODE"></span><span id="cmd_setscanmode"></span>CMD\_SETSCANMODE  
Called by the WIA Flatbed Driver to set the scan mode -- preview or final -- of the microdriver's device. The **lVal** member of the [**VAL**](https://msdn.microsoft.com/library/windows/hardware/ff548627) structure will contain one of the following values, both of which are defined in *wiamicro.h*:

SCANMODE\_PREVIEWSCAN − Preview scan mode

SCANMODE\_FINALSCAN − Final scan mode

<span id="CMD_SETSTIDEVICEHKEY"></span><span id="cmd_setstidevicehkey"></span>CMD\_SETSTIDEVICEHKEY  
Called by the WIA Flatbed Driver to allow the microdriver to read registry entries in the installed registry section. This command provides the STI device's installed registry HKEY to the microdriver, so that it can access private registry values for its device. The **pHandle** member of the [**VAL**](https://msdn.microsoft.com/library/windows/hardware/ff548627) structure will contain a pointer to the HKEY given to the WIA Flatbed Driver during STI's [**IStiUSD::Initialize**](https://msdn.microsoft.com/library/windows/hardware/ff543824) method. This is the top-level HKEY of the installed device section. The **DeviceData** key can be opened directly using this HKEY. See [INF Files for WIA Devices](https://msdn.microsoft.com/library/windows/hardware/ff542770) for more information.

Note: This key is opened and closed *only* by the WIA Flatbed Driver. It is also valid only during this command and CMD\_INITIALIZE (see [Required Commands](required-commands.md)). After those commands return, the key is no longer valid. The HKEY value *must not* be cached.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Optional%20Commands%20%20RELEASE:%20%2811/13/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




