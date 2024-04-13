---
title: Optional Commands
description: Describes commands that can be implemented by the microdriver but are not required.
ms.date: 09/28/2021
---

# Optional Commands

The following commands can be implemented by the microdriver, but it is not required to do so.

## CMD_GETSUPPORTEDFILEFORMATS  

Called by the WIA Flatbed Driver to get the number of additional file formats. Two members of the passed [**VAL**](/windows-hardware/drivers/ddi/wiamicro/ns-wiamicro-val) structure should be filled in: **lVal** should be set to the number of additional file formats; **pGuid** should point to an array of image format GUIDs. The memory allocated for this array is owned by the microdriver and should only be freed by it.

Image formats are listed in *wiadef.h* or can be defined as custom formats. Note that because the BMP (file) and MEMORYBMP (memory) formats are required formats, the WIA Flatbed Driver automatically adds them. The microdriver should not add them to its extended list.

This command is optional unless the device can support extra file formats.

## CMD_GETSUPPORTEDMEMORYFORMATS  

Called by the WIA Flatbed Driver to get the number of additional memory formats. Two members of the passed [**VAL**](/windows-hardware/drivers/ddi/wiamicro/ns-wiamicro-val) structure should be filled in: **lVal** should be set to the number of additional memory formats; **pGuid** should point to an array of image format GUIDs. The memory allocated for this array is owned by the microdriver and should only be freed by it.

Image formats are listed in *wiadef.h* or can be defined as custom formats. Note that because the BMP (file) and MEMORYBMP (memory) formats are required formats, the WIA Flatbed Driver automatically adds them. The microdriver should not add them to its extended list.

This command is optional unless the device can support extra memory formats.

## CMD_SETFORMAT  

The class driver sends this command to set the current format as requested by the application. The **pGuid** member of the [**VAL**](/windows-hardware/drivers/ddi/wiamicro/ns-wiamicro-val) structure contains the image format GUID. The microdriver should save this image format ID in its private context, in order to keep track of the current image format setting.

Microdrivers are required to support this command only if they report extended formats. Because the class driver has no way of validating data in extended formats, it is the microdriver's responsibility to generate the proper data. When transferring data in an extended format, all data should be transferred, including image headers. For example, if your driver reports that it supports the JPEG format, then all of the JPEG must be transferred, not just the image bits.

The class driver owns the memory pointed to by the **pGuid** member of the VAL structure, so the microdriver must not free it.

Note that this command does not affect the way a microdriver responds to calls to its [**Scan**](/windows-hardware/drivers/ddi/wiamicro/nf-wiamicro-scan) function. As usual, the microdriver must check the values of the *lPhase*, *pScanInfo*, and *lLength* parameters of this function, and place data in the buffers pointed to by the *pBuffer* and *pReceived* parameters as appropriate.

Drivers that support only files in the WiaImgFmt_BMP and WiaImgFmt_MEMORYBMP formats (the default formats for microdrivers) can receive the CMD_SETFORMAT command. These drivers can ignore this command, because the class driver handles all data transfers using the default formats.

## CMD_SETSCANMODE  

Called by the WIA Flatbed Driver to set the scan mode -- preview or final -- of the microdriver's device. The **lVal** member of the [**VAL**](/windows-hardware/drivers/ddi/wiamicro/ns-wiamicro-val) structure will contain one of the following values, both of which are defined in *wiamicro.h*:

- SCANMODE_PREVIEWSCAN − Preview scan mode

- SCANMODE_FINALSCAN − Final scan mode

## CMD_SETSTIDEVICEHKEY  

Called by the WIA Flatbed Driver to allow the microdriver to read registry entries in the installed registry section. This command provides the STI device's installed registry HKEY to the microdriver, so that it can access private registry values for its device. The **pHandle** member of the [**VAL**](/windows-hardware/drivers/ddi/wiamicro/ns-wiamicro-val) structure will contain a pointer to the HKEY given to the WIA Flatbed Driver during STI's [**IStiUSD::Initialize**](/windows-hardware/drivers/ddi/stiusd/nf-stiusd-istiusd-initialize) method. This is the top-level HKEY of the installed device section. The **DeviceData** key can be opened directly using this HKEY. See [INF Files for WIA Devices](./inf-files-for-wia-devices.md) for more information.

> [!NOTE]
> This key is opened and closed *only* by the WIA Flatbed Driver. It is also valid only during this command and CMD_INITIALIZE (see [Required Commands](required-commands.md)). After those commands return, the key is no longer valid. The HKEY value *must not* be cached.
