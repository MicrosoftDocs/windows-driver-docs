---
Description: Installing the WpdHelloWorldDriver Sample
MS-HAID: 'wpddk.the\_wpdhelloworlddriver\_installation'
MSHAttr: 'PreferredLib:/library/windows/hardware'
title: Installing the WpdHelloWorldDriver Sample
---

# Installing the WpdHelloWorldDriver Sample


Similar to the other WPD samples, this sample driver installs as a root-enumerated device. It appears under the **Portable Devices** or **WPD** node in **Device Manager**, with a device ID of ROOT\\WPD\\NNNN.

### <span id="Driver_Installation_Steps"></span><span id="driver_installation_steps"></span><span id="DRIVER_INSTALLATION_STEPS"></span>Driver Installation Steps

The following list identifies the steps you should accomplish in order to install the sample driver:

1.  Launch the desired build environment from the **Start** menu.
2.  Build the sample (“build –cZ”).
3.  Copy the UMDF co-installer, *WUDFUpdate\_0xxxx.dll*, to the directory that contains the driver DLL. The co-installer can be found in the &lt;WDK Install Path&gt;\\redist\\wdf\\&lt;architecture&gt; directory.
4.  Install the driver (“devcon install wpdhelloworlddriver.inf WUDF\\WpdHelloWorld”)

Be aware that the last argument to the devcon command corresponds to the following entry that is found in the driver's INF file.

```ManagedCPlusPlus
[Microsoft.NTx86]
%BasicDeviceName%=Basic_Install,WUDF\WpdHelloWorld
```

### <span id="Driver_Removal_Steps"></span><span id="driver_removal_steps"></span><span id="DRIVER_REMOVAL_STEPS"></span>Driver Removal Steps

The following list identifies the steps you should accomplish to remove the sample driver.

1.  Open the Windows Device Manager.
2.  Click the driver under the **Portable Devices** node.
3.  Click **Uninstall**.

## <span id="related_topics"></span>Related topics


****
[The WpdHelloWorldDriverSample](the-sample-driver-architecture.md)

[The WPD Driver Samples](the-wpd-driver-samples.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[wpd_dk\wpddk]:%20Installing%20the%20WpdHelloWorldDriver%20Sample%20%20RELEASE:%20%281/5/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




