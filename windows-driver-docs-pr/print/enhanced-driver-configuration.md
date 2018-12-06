---
title: Enhanced Driver Configuration
description: GPD and PPD files can be used to provide enhanced driver configuration information for a v4 print driver.
ms.assetid: B208C661-4D5B-467A-8451-4382453EC09A
ms.date: 04/20/2017
ms.localizationpriority: medium
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

```xml
<?xml version='1.0'?>
...
  <Property name='DeviceInfo'>
     <Const name="Category" type="BIDI_STRING" value="DeviceCategory"/> 
     <Value name="QueueProperty" type="BIDI_STRING" accessType="Get" queryKey="Configuration" refreshInterval="60" drvPrinterEvent="true"/> 
  </Property> 
...
```

## Related topics

[V4 Printer Driver Connectivity](v4-printer-driver-connectivity.md)  



