---
Description: Installing the WpdMultiTransportDriver Sample
title: Installing the WpdMultiTransportDriver Sample
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Installing the WpdMultiTransportDriver Sample


Similar to the other WPD samples, this sample driver is installed as a root-enumerated device. It appears under the **Portable Devices** or **WPD** node in **Device Manager**, with a device ID of ROOT\\WPD\\NNNN.

### <span id="Driver_Installation_Steps"></span><span id="driver_installation_steps"></span><span id="DRIVER_INSTALLATION_STEPS"></span>Driver Installation Steps

Complete the following steps to install the sample driver:

1.  Launch the desired build environment from the **Start** menu.
2.  Build the sample (“build –cZ”).
3.  Copy *WUDFUpdate\_0xxxx.dll* to the directory that contains the driver DLL. This can be found in the &lt;WDK Install Path&gt;\\redist\\wdf\\&lt;architecture&gt; directory.
4.  Install the driver (“devcon install wpdmultitransportdriver.inf WUDF\\MultiTransport”).

Be aware that the last argument to the devcon command corresponds to the following entry from the driver's INF file.

```ManagedCPlusPlus
[Microsoft.NTx86]
%BasicDeviceName%=Basic_Install,WUDF\MultiTransport
```

### <span id="Driver_Removal_Steps"></span><span id="driver_removal_steps"></span><span id="DRIVER_REMOVAL_STEPS"></span>Driver Removal Steps

Complete the following steps to remove the sample driver:

1.  Open **Device Manager**.
2.  Under the **Portable Devices** node, click the driver that you want to uninstall.
3.  Click **Uninstall**.

## <span id="related_topics"></span>Related topics


****
[The WpdMultiTransportDriverSample](the-wpdmultitransportdriver-sample.md)

[The WPD Driver Samples](the-wpd-driver-samples.md)

 

 





