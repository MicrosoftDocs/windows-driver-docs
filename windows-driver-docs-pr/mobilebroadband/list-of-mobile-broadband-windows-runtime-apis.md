---
title: List of mobile broadband Windows Runtime APIs
description: List of mobile broadband Windows Runtime APIs
ms.assetid: 45ec97c4-1a58-48a8-ad50-1cd8fcc4763f
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# List of mobile broadband Windows Runtime APIs


The following table lists the APIs for authoring a mobile broadband app.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>API</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><a href="connection-profile-api.md" data-raw-source="[Connection Profile API](connection-profile-api.md)">Connection Profile API</a></p></td>
<td><p>Provides information about the connection status (for example, to the Internet)</p></td>
</tr>
<tr class="even">
<td><p><a href="device-services-extension-api.md" data-raw-source="[Device Services Extension API](device-services-extension-api.md)">Device Services Extension API</a></p></td>
<td><p>Enables device-specific extensions, such as SIM Toolkit and Preferred Roaming List (PRL) download.</p></td>
</tr>
<tr class="odd">
<td><p><a href="provisioning-api.md" data-raw-source="[Provisioning API](provisioning-api.md)">Provisioning API</a></p></td>
<td><p>Enables you to provision Windows with account provisioning data and data usage information.</p></td>
</tr>
<tr class="even">
<td><p><a href="sim-pin-api.md" data-raw-source="[SIM PIN API](sim-pin-api.md)">SIM PIN API</a></p></td>
<td><p>Enables you to enable, disable, or change the SIM PIN.</p></td>
</tr>
<tr class="odd">
<td><p><a href="sms-api.md" data-raw-source="[SMS API](sms-api.md)">SMS API</a></p></td>
<td><p>Provides functions that are required to implement an SMS client.</p></td>
</tr>
<tr class="even">
<td><p><a href="subscriber-and-device-information-api.md" data-raw-source="[Subscriber and Device Information API](subscriber-and-device-information-api.md)">Subscriber and Device Information API</a></p></td>
<td><p>Provides subscriber information for the SIM and device information for the mobile broadband device.</p></td>
</tr>
<tr class="odd">
<td><p><a href="ussd-api.md" data-raw-source="[USSD API](ussd-api.md)">USSD API</a></p></td>
<td><p>Enables you to establish an Unstructured Supplementary Service Data (USSD) session with a network (client and network initiated).</p></td>
</tr>
</tbody>
</table>

 

The following sections are available in this topic:

-   [Mobile Broadband Account API](#mbacctapi)

-   [Network Account IDs](#netid)

## <span id="mbacctapi"></span><span id="MBACCTAPI"></span>Mobile Broadband Account API


Because it has methods that can be used to get personally identifiable information about the customer and change the network settings on mobile broadband devices, the Mobile Broadband Account API is a privileged API. This means that most UWP apps cannot call its methods without getting an “access denied” error. To be able to call this API, a UWP app must meet the following criteria:

-   The app must have a device metadata or service metadata package associated with it, and it must be listed in the [PrivilegedApplications](privilegedapplications.md) XML element of the SoftwareInfo.xml file inside the package. The package does not have to be exclusive to the application; it is possible for any particular UWP app to be listed in the PrivilegedApplications element of several packages. That package must be associated with the service provider for a mobile broadband device that has been active at least once on the computer, so that it has been installed.

-   The application’s appxmanifest file needs a **&lt;DeviceCapability&gt;** entry for the Mobile Broadband Account API. You can do this by adding the following XML element as a child of the **&lt;Capabilities&gt;** element in the application’s appxmanifest file:

    ``` syntax
    <DeviceCapability Name="BFCD56F7-3943-457F-A312-2E19BB6DC648" />
    ```

    For more information on the **&lt;Capabilities&gt;** element, see [App Manifest File For Windows 8](https://msdn.microsoft.com/library/windows/apps/ff769509.aspx).

**Note**  
Applications that are not UWP apps (for example, Microsoft Win32 services or desktop apps) have unrestricted access to the Mobile Broadband Account API. This is because these applications can use existing Win32 and Component Object Model (COM) APIs to get full access to the mobile broadband network. These APIs cannot be used from UWP apps.

 

## <span id="netid"></span><span id="NETID"></span>Network Account IDs


A network account ID is a unique identifier for a mobile broadband account. It provides a unified ID that can be used without needing to know whether the ID comes from a GSM, CDMA, or WiMAX network. Windows generates network account IDs whenever it encounters a hardware-provided network subscription identifier that it has not encountered before. The following list identifies the network account ID for each supported network type:

-   GSM networks: The SIM’s ICCID is used to differentiate between subscriptions.

-   CDMA networks: The mobile identification number (MIN) is used.

When Windows encounters one of the preceding network types for the first time, it creates a new network account ID and maps it to a SHA-256 hash of the hardware-provided subscription identifier, and then stores both of them in the registry. Conversely, if Windows finds the hash of the hardware-provided subscription identifier in the registry, it uses the network account ID that’s associated with that hash. Network account IDs should be globally unique (they are based on GUIDs), but because what is stored is a hash of the hardware-provided identifier, the network hardware must be present when trying to map a network account ID back to the ICCID or MIN that it was generated from.

**Important**  
Even though getting the ICCID from a network account ID requires access to the computer and the network device that are used to map them together, network account IDs do uniquely identify individual users. Therefore, we recommend that you follow your organization’s policies for dealing with personally identifiable information when you're working with them.

 

Network account IDs are segregated by mobile network operator (MNO), so that if an end user has both Provider1 and Provider2 mobile broadband devices and their corresponding mobile broadband apps are installed, the Provider1 app will not be able to use any Provider2 network account IDs, and vice versa. The function that returns all network account IDs will return only the IDs of the network accounts for the MNO whose application is calling the function. An attempt to use a network account ID that belongs to a different MNO will result in an “access denied” error.

**Note**  
Apps that are not UWP apps (for example, Win32 services or desktop apps) have access to all network accounts regardless of network service provider.

 

## <span id="related_topics"></span>Related topics


[Mobile broadband WinRT API overview](mobile-broadband-winrt-api-overview.md)

 

 






