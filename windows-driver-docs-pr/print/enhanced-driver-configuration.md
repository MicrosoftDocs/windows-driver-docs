---
title: Enhanced Driver Configuration
description: GPD and PPD files can be used to provide enhanced driver configuration information for a v4 print driver.
ms.assetid: B208C661-4D5B-467A-8451-4382453EC09A
---

# Enhanced Driver Configuration


GPD and PPD files can be used to provide enhanced driver configuration information for a v4 print driver.

A print driver based on the v4 driver model can then retrieve these GPD and PPD files from the device using Bidi. This allows devices using a print class driver to support a richer feature set without requiring additional downloads from Windows Update.

This functionality is supported by default for drivers that support WS-Print v1.1. However, TCP/IP devices and WS-Print v1.0 devices may also support this functionality by implementing the Bidi extension files that specify the following Bidi schema elements.

**Schema path: schema section for reading the GPD/PPD files**

**Section Name:** DriverConfigFiles

**Schema Path:** \\Printer.Configuration.DriverConfigFiles

**Description:** This new section for the Bidi Schema will contain schema values to query the device for driver configuration data, including the GPD and PPD description files.

Extension for Reading the GPD File

**Schema Name:** GPDFile

**Schema Path:** \\Printer.Configuration.DriverConfigFiles:GPDFile

**Node Type:** Value

**Data Type:** BIDI\_STRING

**Description:** The full GPD file for the device. This contains all the specific device configuration information that is available and up to date according to the current settings of the device.

Extension for Reading the PPD File

**Schema Name:** PPDFile

**Schema Path:** \\Printer.Configuration.DriverConfigFiles:PPDFile

**Node Type:** Value

**Data Type:** BIDI\_STRING

**Description:** The full PPD file for the device. This contains all the specific device configuration information that is available and up to date according to the current settings of the device.

**Note**  For USB devices, whether you're using a GPD or a PPD file, the Bidi extension XML file must specify the drvPrinterEvent attribute and set its value to "true". This ensures that the element is updated after Bidi cache refreshes.

 

The following XML fragment demonstrates the correct syntax for using the drvPrinterEvent attribute:

```XML
<?xml vesrion=&#39;1.0&#39;?>
...
  <Property name=&#39;DeviceInfo&#39;>
     <Const name="Category" type="BIDI_STRING" value="DeviceCategory"/> 
     <Value name="QueueProperty" type="BIDI_STRING" accessType="Get" queryKey="Configuration" refreshInterval="60" drvPrinterEvent="true"/> 
  </Property> 
...
```

## Related topics


[V4 Printer Driver Connectivity](v4-printer-driver-connectivity.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Enhanced%20Driver%20Configuration%20%20RELEASE:%20%283/29/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





