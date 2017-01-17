---
Description: Installing the Sample Driver
MS-HAID: 'wpddk.the\_wpdbasichardwaredriver\_installation'
MSHAttr: 'PreferredLib:/library/windows/hardware'
title: Installing the Sample Driver
---

# Installing the Sample Driver


Similar to the other Windows Portable Devices (WPD) samples, this sample driver installs as a root-enumerated device. It appears under the Portable Devices or WPD node in **Device Manager**, and has a device ID of ROOT\\WPD\\NNNN.

When you install a root-enumerated device, you get a device that is always connected. As a result, even if the sensor device is unplugged from the RS-232 port, the device node (devnode) is not removed. To support devnode arrival (or removal) when the RS-232 connection is plugged in (or unplugged), you must supply a Plug and Play (PnP) bus enumerator. A sample bus enumerator is provided with the WDK Toaster Sample.

The installation INF file for the sample driver is based on the INF file for WpdHelloWorldDriver. Most of the changes involve string replacement of WpdHelloWorldDriver with WpdBasicHardwareDriver. The more significant changes are summarized in the following sections.

### <span id="Enabling_File-Handle_Targets"></span><span id="enabling_file-handle_targets"></span><span id="ENABLING_FILE-HANDLE_TARGETS"></span>Enabling File-Handle Targets

The following entry is added under \[*Basic\_Install.Wdf*\] to enable file handle–based UMDF I/O targets. These I/O targets are used to exchange data with the device by using the RS 232 port. For more information about I/O targets, see [Supporting I/O](the-wpdbasichardwaredriver-supporting-io.md).

```
UmdfDispatcher = FileHandle
```

### <span id="Disabling_Legacy_WIA_Support"></span><span id="disabling_legacy_wia_support"></span><span id="DISABLING_LEGACY_WIA_SUPPORT"></span>Disabling Legacy WIA Support

The following line is commented out to disable Windows Image Acquisition (WIA) legacy applications from accessing this driver because the sample driver does not support image content:

```
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[wpd_dk\wpddk]:%20Installing%20the%20Sample%20Driver%20%20RELEASE:%20%281/5/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




