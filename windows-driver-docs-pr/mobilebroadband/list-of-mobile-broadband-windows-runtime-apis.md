---
title: List of mobile broadband Windows Runtime APIs
description: List of mobile broadband Windows Runtime APIs
ms.assetid: 45ec97c4-1a58-48a8-ad50-1cd8fcc4763f
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
<td><p>[Connection Profile API](connection-profile-api.md)</p></td>
<td><p>Provides information about the connection status (for example, to the Internet)</p></td>
</tr>
<tr class="even">
<td><p>[Device Services Extension API](device-services-extension-api.md)</p></td>
<td><p>Enables device-specific extensions, such as SIM Toolkit and Preferred Roaming List (PRL) download.</p></td>
</tr>
<tr class="odd">
<td><p>[Provisioning API](provisioning-api.md)</p></td>
<td><p>Enables you to provision Windows with account provisioning data and data usage information.</p></td>
</tr>
<tr class="even">
<td><p>[SIM PIN API](sim-pin-api.md)</p></td>
<td><p>Enables you to enable, disable, or change the SIM PIN.</p></td>
</tr>
<tr class="odd">
<td><p>[SMS API](sms-api.md)</p></td>
<td><p>Provides functions that are required to implement an SMS client.</p></td>
</tr>
<tr class="even">
<td><p>[Subscriber and Device Information API](subscriber-and-device-information-api.md)</p></td>
<td><p>Provides subscriber information for the SIM and device information for the mobile broadband device.</p></td>
</tr>
<tr class="odd">
<td><p>[USSD API](ussd-api.md)</p></td>
<td><p>Enables you to establish an Unstructured Supplementary Service Data (USSD) session with a network (client and network initiated).</p></td>
</tr>
</tbody>
</table>

 

The following sections are available in this topic:

-   [Mobile Broadband Account API](#mbacctapi)

-   [Network Account IDs](#netid)

## <span id="mbacctapi"></span><span id="MBACCTAPI"></span>Mobile Broadband Account API


Because it has methods that can be used to get personally identifiable information about the customer and change the network settings on mobile broadband devices, the Mobile Broadband Account API is a privileged API. This means that most Windows Store apps cannot call its methods without getting an “access denied” error. To be able to call this API, a Windows Store app must meet the following criteria:

-   The app must have a device metadata or service metadata package associated with it, and it must be listed in the [PrivilegedApplications](privilegedapplications.md) XML element of the SoftwareInfo.xml file inside the package. The package does not have to be exclusive to the application; it is possible for any particular Windows Store app to be listed in the PrivilegedApplications element of several packages. That package must be associated with the service provider for a mobile broadband device that has been active at least once on the computer, so that it has been installed.

-   The application’s appxmanifest file needs a **&lt;DeviceCapability&gt;** entry for the Mobile Broadband Account API. You can do this by adding the following XML element as a child of the **&lt;Capabilities&gt;** element in the application’s appxmanifest file:

    ``` syntax
    <DeviceCapability Name="BFCD56F7-3943-457F-A312-2E19BB6DC648" />
    ```

    For more information on the **&lt;Capabilities&gt;** element, see [App Manifest File For Windows 8](https://msdn.microsoft.com/library/windows/apps/ff769509.aspx).

**Note**  
Applications that are not Windows Store apps (for example, Microsoft Win32 services or desktop apps) have unrestricted access to the Mobile Broadband Account API. This is because these applications can use existing Win32 and Component Object Model (COM) APIs to get full access to the mobile broadband network. These APIs cannot be used from Windows Store apps.

 

## <span id="netid"></span><span id="NETID"></span>Network Account IDs


A network account ID is a unique identifier for a mobile broadband account. It provides a unified ID that can be used without needing to know whether the ID comes from a GSM, CDMA, or WiMAX network. Windows generates network account IDs whenever it encounters a hardware-provided network subscription identifier that it has not encountered before. The following list identifies the network account ID for each supported network type:

-   GSM networks: The SIM’s ICCID is used to differentiate between subscriptions.

-   CDMA networks: The mobile identification number (MIN) is used.

When Windows encounters one of the preceding network types for the first time, it creates a new network account ID and maps it to a SHA-256 hash of the hardware-provided subscription identifier, and then stores both of them in the registry. Conversely, if Windows finds the hash of the hardware-provided subscription identifier in the registry, it uses the network account ID that’s associated with that hash. Network account IDs should be globally unique (they are based on GUIDs), but because what is stored is a hash of the hardware-provided identifier, the network hardware must be present when trying to map a network account ID back to the ICCID or MIN that it was generated from.

**Important**  
Even though getting the ICCID from a network account ID requires access to the computer and the network device that are used to map them together, network account IDs do uniquely identify individual users. Therefore, we recommend that you follow your organization’s policies for dealing with personally identifiable information when you're working with them.

 

Network account IDs are segregated by mobile network operator (MNO), so that if an end user has both Provider1 and Provider2 mobile broadband devices and their corresponding mobile broadband apps are installed, the Provider1 app will not be able to use any Provider2 network account IDs, and vice versa. The function that returns all network account IDs will return only the IDs of the network accounts for the MNO whose application is calling the function. An attempt to use a network account ID that belongs to a different MNO will result in an “access denied” error.

**Note**  
Apps that are not Windows Store apps (for example, Win32 services or desktop apps) have access to all network accounts regardless of network service provider.

 

## <span id="related_topics"></span>Related topics


[Mobile broadband WinRT API overview](mobile-broadband-winrt-api-overview.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20List%20of%20mobile%20broadband%20Windows%20Runtime%20APIs%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





