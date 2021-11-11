---
title: Required Commands
description: Describes required commands that must be implemented by every microdriver.
ms.date: 09/28/2021
ms.localizationpriority: medium
---

# Required Commands

The following set of required commands must be implemented by every microdriver.

## CMD_GETCAPABILITIES  

Called by the WIA Flatbed Driver to get button event information. Three members of the passed [**VAL**](/windows-hardware/drivers/ddi/wiamicro/ns-wiamicro-val) structure should be filled in: **lVal** should be set to the number of buttons; **pGuid** should be set to an array of event GUIDs; **ppButtonNames** can optionally be set to a **WCHAR**\* array that contains the button names in the same order as they are in **pGuid** (for example, "Scan Button" or "Fax Button"). If **ppButtonNames** is set to **NULL**, the WIA Flatbed Driver will create generic button names. The arrays can be allocated in response to CMD_INITIALIZE, and freed in CMD_UNINITIALIZE.

## CMD_INITIALIZE  

Called by the WIA Flatbed Driver to initialize the microdriver and set device I/O handles to valid values. This command will be sent to the microdriver when the WIA service calls the method [**IWiaMiniDrv::drvInitializeWia**](/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiaminidrv-drvinitializewia) on the WIA Flatbed Driver.

The WIA Flatbed Driver will automatically create one device I/O handle and put it in the **DeviceIOHandles** array member of the passed [**SCANINFO**](/windows-hardware/drivers/ddi/wiamicro/ns-wiamicro-_scaninfo) structure at index 0. The microdriver should use this handle when it needs to communicate with the device. If the microdriver needs additional device handles (for example, to use multiple bulk USB pipes), they can be created and stored in the **DeviceIOHandles** array up to a maximum number of MAX_IO_HANDLES. The WIA Flatbed Driver will automatically close the handle at index 0, because it created that handle during initialization. The other handles must be closed by the microdriver in response to CMD_UNINITIALIZE.

As part of this command, the microdriver should also initialize all of the values in the [**SCANINFO**](/windows-hardware/drivers/ddi/wiamicro/ns-wiamicro-_scaninfo) structure. The microdriver should set the **SupportedDataTypes**, **IntensityRange**, **ContrastRange**, **BedWidth**, and **BedHeight** members of the SCANINFO structure, so that the WIA Flatbed Driver can automatically validate these values against the legal ranges for the device.

## CMD_RESETSCANNER  

Called by the WIA Flatbed Driver to reset the device in response to a WIA service request. The microdriver should set the device to its power-on state. In Windows Vista, the WIA Flatbed Driver does not use this command. However, microdrivers should continue to support this command to ensure correct operation in Windows XP and, possibly, with a future version of the WIA Flatbed Driver that might use this command.

## CMD_SETDATATYPE  

Called by the WIA Flatbed Driver to set the data type for the scan. One of the following values is passed in the **lVal** member of the passed [**VAL**](/windows-hardware/drivers/ddi/wiamicro/ns-wiamicro-val) structure:

- WIA_DATA_THRESHOLD − 1-bit black/white

- WIA_DATA_GRAYSCALE − 8-bit grayscale

- WIA_DATA_COLOR − 24-bit color

The microdriver should store the value in the **DataType** member of the passed [**SCANINFO**](/windows-hardware/drivers/ddi/wiamicro/ns-wiamicro-_scaninfo) structure.

## CMD_SETCONTRAST  

Called by the WIA Flatbed Driver to set the contrast value for the scan. The desired contrast value is passed in the **lVal** member of the passed [**VAL**](/windows-hardware/drivers/ddi/wiamicro/ns-wiamicro-val) structure. The value −1000 should be interpreted as the lowest contrast value, 0 nominal, and 1000 the device's maximum contrast. The microdriver should store the value in the **Contrast** member of the passed [**SCANINFO**](/windows-hardware/drivers/ddi/wiamicro/ns-wiamicro-_scaninfo) structure.

## CMD_SETINTENSITY  

Called by the WIA Flatbed Driver to set the intensity or brightness value for the scan. The desired intensity value is passed in the **lVal** member of the passed [**VAL**](/windows-hardware/drivers/ddi/wiamicro/ns-wiamicro-val) structure. The value −1000 should be interpreted as the lowest brightness value, 0 nominal, and 1000 the device's maximum brightness. The microdriver should store the value in the **Intensity** member of the passed [**SCANINFO**](/windows-hardware/drivers/ddi/wiamicro/ns-wiamicro-_scaninfo) structure.

## CMD_SETXRESOLUTION  

Called by the WIA Flatbed Driver to set the horizontal scan resolution. The desired resolution in pixels is passed in the **lVal** member of the passed [**VAL**](/windows-hardware/drivers/ddi/wiamicro/ns-wiamicro-val) structure. The microdriver should store the value in the **XResolution** member of the passed [**SCANINFO**](/windows-hardware/drivers/ddi/wiamicro/ns-wiamicro-_scaninfo) structure.

## CMD_SETYRESOLUTION  

Called by the WIA Flatbed Driver to set the vertical scan resolution. The desired resolution in pixels is passed in the **lVal** member of the passed VAL structure. The microdriver should store the value in the **YResolution** member of the passed SCANINFO structure.

## CMD_STI_DEVICERESET  

Called by the WIA Flatbed Driver to reset the device in response to a Still Image (STI) request. This command is typically called only once, during initialization.

## CMD_STI_DIAGNOSTIC  

Called by the WIA Flatbed Driver when the user requests a test of the device.

## CMD_UNINITIALIZE  

Uninitialize the microdriver and close Device I/O handles. The WIA Flatbed Driver will automatically close the device I/O handle in the **DeviceIOHandles** array member of the [**SCANINFO**](/windows-hardware/drivers/ddi/wiamicro/ns-wiamicro-_scaninfo) structure, at index 0. This command will be sent to the microdriver when the WIA Flatbed driver is unloading.
