---
Description: Installing the WpdHelloWorldDriver Sample
title: Installing the WpdHelloWorldDriver Sample
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 





