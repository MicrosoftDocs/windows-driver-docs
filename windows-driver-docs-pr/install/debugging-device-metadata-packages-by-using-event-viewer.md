---
title: Debugging Device Metadata Packages By Using Event Viewer
description: Debugging Device Metadata Packages By Using Event Viewer
ms.assetid: 168a9dd1-aab2-4497-a59d-b8fe52d8cde2
---

# Debugging Device Metadata Packages By Using Event Viewer


Starting with Windows 7, the Event Tracing for Windows (ETW) service supports the DeviceMetadata/Debug channel for events that are related to the processing of device metadata packages.

The DeviceMetadata/Debug channel stores error and informational events that occur during the download or processing of device metadata packages. This channel also stores warning and informational events that provide additional status about the detection and query of device metadata packages within the [device metadata store](device-metadata-store.md).

### Viewing Device Metadata/Debug ETW Events through Event Viewer

You use Event Viewer to view events that are logged for device metadata packages. Follow these steps to open the DeviceMetadata/Debug ETW channel in Event Viewer to view these events:

1.  On the **Start** menu, right-click **Computer**, and then click **Manage**.

2.  Expand the **System Tools** node.

3.  Expand and then click the **Event Viewer** node.

4.  On the **View** menu, click **Show Analytic and Debug Logs**.

5.  Expand the **Applications and Services Logs** node.

6.  Expand the **Microsoft** node.

7.  Expand the **Windows** node.

8.  Expand the **UserPnP** node.

9.  Click the **DeviceMetadata/Debug** node.

    **Note**  You must first enable logging on the DeviceMetadata/Debug ETW channel to receive and view events. To do this, right-click the **DeviceMetadata/Debug** node and select **Properties**. Then, click **Enable Log**.

     

### Device Metadata/Debug ETW Events

The operating system logs the following error, warning, and informational events during the download or processing of a device metadata package:

<a href="" id="event-id--7900-error--device-metadata-package-error"></a>Event ID: 7900 Error: Device metadata package error  
An error was detected with one of the components of a device metadata package.

This event log message contains the following information:

-   A description of the error, which includes a description of the source of the error. The error source is either the [device metadata store](device-metadata-store.md) or the [device metadata cache](device-metadata-cache.md).

-   The name of the device metadata package.

-   An application-specific error code. For more information about these error codes, see [Device Metadata Error Codes](device-metadata-error-codes.md).

-   A Win32 error code.

<a href="" id="event-id--7901-information--device-metadata-package-downloaded-from-wmis-"></a>Event ID: 7901 Information: Device metadata package downloaded from WMIS.  
A device metadata package was downloaded from the [Windows Metadata and Internet Services](windows-metadata-and-internet-services.md) (WMIS) by the [Device Metadata Retrieval Client](device-metadata-retrieval-client.md) (DMRC), which extracts the components from the package and saves them within the [device metadata cache](device-metadata-cache.md).

This event log message contains the following information:

-   A description of the event.

-   The location of the unpacked device metadata package within the [device metadata cache](device-metadata-cache.md).

-   The name of the device metadata package.

<a href="" id="event-id--7902-error--device-metadata-package-not-signed--"></a>Event ID: 7902 Error: Device metadata package not signed.   
An installed device metadata package was not signed by the [Windows Quality Online Services (Winqual)](http://go.microsoft.com/fwlink/p/?linkid=62651).

**Note**  The signature of the device metadata package is verified only when it is downloaded from WMIS.

 

This event log message contains the following information:

-   A description of the error.

-   The name of the device metadata package.

-   An application-specific error code. For more information about these error codes, see [Device Metadata Error Codes](device-metadata-error-codes.md).

-   A Win32 error code.

<a href="" id="event-id--7950-information--new-device-metadata-package-discovered-in-the-local-metadata-store-"></a>Event ID: 7950 Information: New device metadata package discovered in the local metadata store.  
The DMRC has detected a new device metadata package that is installed on the local computer.

This event log message contains the following information:

-   A description of the event.

-   The source of the device metadata package, which is either the [device metadata store](device-metadata-store.md) or the [device metadata cache](device-metadata-cache.md).

-   The name of the device metadata package.

<a href="" id="event-id--7951-information--query-for-metadata-packages-in-progress-"></a>Event ID: 7951 Information: Query for metadata packages in progress.  
The DMRC queries installed device metadata packages for a particular device.

This event log message contains the following information:

-   A description of the event.

-   A device lookup key, such as the device's hardware ID or model ID. For more information, see [**HardwareID**](https://msdn.microsoft.com/library/windows/hardware/ff546114) and [**ModelID**](https://msdn.microsoft.com/library/windows/hardware/ff549295).

    **Note**   Only the most specific hardware ID is logged when a list of hardware IDs are passed as a parameter.

     

<a href="" id="event-id--7952-warning--network-related-errors-"></a>Event ID: 7952 Warning: Network-related errors.  
The DMRC encountered a network error during the download of a device metadata packaged from the WMIS.

**Note**   This warning is not generated when the network is not available.

 

This event log message contains the following information:

-   A detailed description of the error.

-   An application-specific error code. For more information about these error codes, see [Device Metadata Error Codes](device-metadata-error-codes.md).

-   The HTTP status code at the time of the network error.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Debugging%20Device%20Metadata%20Packages%20By%20Using%20Event%20Viewer%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




