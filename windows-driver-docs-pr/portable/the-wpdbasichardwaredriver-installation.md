---
Description: Installing the Sample Driver
title: Installing the Sample Driver
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Installing the Sample Driver


Similar to the other Windows Portable Devices (WPD) samples, this sample driver installs as a root-enumerated device. It appears under the Portable Devices or WPD node in **Device Manager**, and has a device ID of ROOT\\WPD\\NNNN.

When you install a root-enumerated device, you get a device that is always connected. As a result, even if the sensor device is unplugged from the RS-232 port, the device node (devnode) is not removed. To support devnode arrival (or removal) when the RS-232 connection is plugged in (or unplugged), you must supply a Plug and Play (PnP) bus enumerator. A sample bus enumerator is provided with the WDK Toaster Sample.

The installation INF file for the sample driver is based on the INF file for WpdHelloWorldDriver. Most of the changes involve string replacement of WpdHelloWorldDriver with WpdBasicHardwareDriver. The more significant changes are summarized in the following sections.

### <span id="Enabling_File-Handle_Targets"></span><span id="enabling_file-handle_targets"></span><span id="ENABLING_FILE-HANDLE_TARGETS"></span>Enabling File-Handle Targets

The following entry is added under \[*Basic\_Install.Wdf*\] to enable file handle–based UMDF I/O targets. These I/O targets are used to exchange data with the device by using the RS 232 port. For more information about I/O targets, see [Supporting I/O](the-wpdbasichardwaredriver-supporting-io.md).

```cpp
UmdfDispatcher = FileHandle
```

### <span id="Disabling_Legacy_WIA_Support"></span><span id="disabling_legacy_wia_support"></span><span id="DISABLING_LEGACY_WIA_SUPPORT"></span>Disabling Legacy WIA Support

The following line is commented out to disable Windows Image Acquisition (WIA) legacy applications from accessing this driver because the sample driver does not support image content:

```cpp
;HKR,,”EnableLegacySupport”,0x10001,1
```

### <span id="Installing_the_Driver"></span><span id="installing_the_driver"></span><span id="INSTALLING_THE_DRIVER"></span>Installing the Driver

To install the sample driver, complete the following steps:

1.  From the **Start** menu, open the desired build environment .
2.  Build the sample (“build –cZ”).
3.  Copy *WUDFUpdate\_0xxxx.dll* from the &lt;WDK Install Location&gt;\\redist\\wdf\\&lt;architecture&gt; directory to the directory that contains the DLL for the driver.
4.  Install the driver (“devcon install *Wpdbasichardwaredriver.inf* WUDF\\WpdBasicHardware”)

**Note**  The last argument to the devcon command corresponds to the following excerpt from the driver's INF file.

 

```ManagedCPlusPlus
[Microsoft.NTx86]
%BasicDeviceName%=Basic_Install,WUDF\WpdBasicHardware
```

### <span id="Removing_the_Driver"></span><span id="removing_the_driver"></span><span id="REMOVING_THE_DRIVER"></span>Removing the Driver

To remove the sample driver, complete the following steps:

1.  Open Windows Device Manager.
2.  Right-click the driver under the **Portable Devices** node, and click **Uninstall**.

## <span id="related_topics"></span>Related topics


****
[The WpdBasicHardwareDriverSample](the-wpdbasichardwaredriver-sample.md)

[The WPD Driver Samples](the-wpd-driver-samples.md)

 

 





