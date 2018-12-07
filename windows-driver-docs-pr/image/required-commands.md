---
title: Required Commands
description: Required Commands
ms.assetid: e4a82cc6-8031-4d67-bef8-1d73e2d98b6b
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# Required Commands


## <span id="ddk_required_commands_si"></span><span id="DDK_REQUIRED_COMMANDS_SI"></span>


The following set of required commands must be implemented by every microdriver.

<span id="CMD_GETCAPABILITIES"></span><span id="cmd_getcapabilities"></span>CMD\_GETCAPABILITIES  
Called by the WIA Flatbed Driver to get button event information. Three members of the passed [**VAL**](https://msdn.microsoft.com/library/windows/hardware/ff548627) structure should be filled in: **lVal** should be set to the number of buttons; **pGuid** should be set to an array of event GUIDs; **ppButtonNames** can optionally be set to a **WCHAR**\* array that contains the button names in the same order as they are in **pGuid** (for example, "Scan Button" or "Fax Button"). If **ppButtonNames** is set to **NULL**, the WIA Flatbed Driver will create generic button names. The arrays can be allocated in response to CMD\_INITIALIZE, and freed in CMD\_UNINITIALIZE.

<span id="CMD_INITIALIZE"></span><span id="cmd_initialize"></span>CMD\_INITIALIZE  
Called by the WIA Flatbed Driver to initialize the microdriver and set device I/O handles to valid values. This command will be sent to the microdriver when the WIA service calls the method [**IWiaMiniDrv::drvInitializeWia**](https://msdn.microsoft.com/library/windows/hardware/ff544986) on the WIA Flatbed Driver.

The WIA Flatbed Driver will automatically create one device I/O handle and put it in the **DeviceIOHandles** array member of the passed [**SCANINFO**](https://msdn.microsoft.com/library/windows/hardware/ff547361) structure at index 0. The microdriver should use this handle when it needs to communicate with the device. If the microdriver needs additional device handles (for example, to use multiple bulk USB pipes), they can be created and stored in the **DeviceIOHandles** array up to a maximum number of MAX\_IO\_HANDLES. The WIA Flatbed Driver will automatically close the handle at index 0, because it created that handle during initialization. The other handles must be closed by the microdriver in response to CMD\_UNINITIALIZE.

As part of this command, the microdriver should also initialize all of the values in the [**SCANINFO**](https://msdn.microsoft.com/library/windows/hardware/ff547361) structure. The microdriver should set the **SupportedDataTypes**, **IntensityRange**, **ContrastRange**, **BedWidth**, and **BedHeight** members of the SCANINFO structure, so that the WIA Flatbed Driver can automatically validate these values against the legal ranges for the device.

<span id="CMD_RESETSCANNER"></span><span id="cmd_resetscanner"></span>CMD\_RESETSCANNER  
Called by the WIA Flatbed Driver to reset the device in response to a WIA service request. The microdriver should set the device to its power-on state. In Windows Vista, the WIA Flatbed Driver does not use this command. However, microdrivers should continue to support this command to ensure correct operation in Windows XP and, possibly, with a future version of the WIA Flatbed Driver that might use this command.

<span id="CMD_SETDATATYPE"></span><span id="cmd_setdatatype"></span>CMD\_SETDATATYPE  
Called by the WIA Flatbed Driver to set the data type for the scan. One of the following values is passed in the **lVal** member of the passed [**VAL**](https://msdn.microsoft.com/library/windows/hardware/ff548627) structure:

WIA\_DATA\_THRESHOLD − 1-bit black/white

WIA\_DATA\_GRAYSCALE − 8-bit grayscale

WIA\_DATA\_COLOR − 24-bit color

The microdriver should store the value in the **DataType** member of the passed [**SCANINFO**](https://msdn.microsoft.com/library/windows/hardware/ff547361) structure.

<span id="CMD_SETCONTRAST"></span><span id="cmd_setcontrast"></span>CMD\_SETCONTRAST  
Called by the WIA Flatbed Driver to set the contrast value for the scan. The desired contrast value is passed in the **lVal** member of the passed [**VAL**](https://msdn.microsoft.com/library/windows/hardware/ff548627) structure. The value −1000 should be interpreted as the lowest contrast value, 0 nominal, and 1000 the device's maximum contrast. The microdriver should store the value in the **Contrast** member of the passed [**SCANINFO**](https://msdn.microsoft.com/library/windows/hardware/ff547361) structure.

<span id="CMD_SETINTENSITY"></span><span id="cmd_setintensity"></span>CMD\_SETINTENSITY  
Called by the WIA Flatbed Driver to set the intensity or brightness value for the scan. The desired intensity value is passed in the **lVal** member of the passed [**VAL**](https://msdn.microsoft.com/library/windows/hardware/ff548627) structure. The value −1000 should be interpreted as the lowest brightness value, 0 nominal, and 1000 the device's maximum brightness. The microdriver should store the value in the **Intensity** member of the passed [**SCANINFO**](https://msdn.microsoft.com/library/windows/hardware/ff547361) structure.

<span id="CMD_SETXRESOLUTION"></span><span id="cmd_setxresolution"></span>CMD\_SETXRESOLUTION  
Called by the WIA Flatbed Driver to set the horizontal scan resolution. The desired resolution in pixels is passed in the **lVal** member of the passed [**VAL**](https://msdn.microsoft.com/library/windows/hardware/ff548627) structure. The microdriver should store the value in the **XResolution** member of the passed [**SCANINFO**](https://msdn.microsoft.com/library/windows/hardware/ff547361) structure.

<span id="CMD_SETYRESOLUTION"></span><span id="cmd_setyresolution"></span>CMD\_SETYRESOLUTION  
Called by the WIA Flatbed Driver to set the vertical scan resolution. The desired resolution in pixels is passed in the **lVal** member of the passed VAL structure. The microdriver should store the value in the **YResolution** member of the passed SCANINFO structure.

<span id="CMD_STI_DEVICERESET"></span><span id="cmd_sti_devicereset"></span>CMD\_STI\_DEVICERESET  
Called by the WIA Flatbed Driver to reset the device in response to a Still Image (STI) request. This command is typically called only once, during initialization.

<span id="CMD_STI_DIAGNOSTIC"></span><span id="cmd_sti_diagnostic"></span>CMD\_STI\_DIAGNOSTIC  
Called by the WIA Flatbed Driver when the user requests a test of the device.

<span id="CMD_UNINITIALIZE"></span><span id="cmd_uninitialize"></span>CMD\_UNINITIALIZE  
Uninitialize the microdriver and close Device I/O handles. The WIA Flatbed Driver will automatically close the device I/O handle in the **DeviceIOHandles** array member of the [**SCANINFO**](https://msdn.microsoft.com/library/windows/hardware/ff547361) structure, at index 0. This command will be sent to the microdriver when the WIA Flatbed driver is unloading.

 

 





