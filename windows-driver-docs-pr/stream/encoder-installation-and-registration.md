---
title: Encoder Installation and Registration
description: Encoder Installation and Registration
ms.assetid: 6ce0c504-977a-4db5-b5ee-128b69ce8eba
keywords:
- kernel streaming categories WDK encoder
- encoder devices WDK AVStream
- AVStream WDK , encoder devices
- uncompressed data streams WDK AVStream
- encoded streams WDK AVStream
- audio encoder devices WDK AVStream
- video encoder devices WDK AVStream
- INF files WDK encoder
- metadata WDK encoder
- KS proxy WDK AVStream
- Kernel Streaming Proxy WDK AVStream
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Encoder Installation and Registration


The INF file for a driver with an encoder filter must contain entries that define the following:

-   Additional kernel streaming capture components

-   Which COM interface KsProxy should expose

-   Metadata values that describe the encoder filter's capabilities

-   The filter's kernel streaming category

### **Additional Kernel Streaming Capture Components**

The INF file used to install the driver for an encoder device must reference *ks.inf* and *kscaptur.inf* in its \[DefaultInstall\] section as capture drivers because these files add necessary support for encoder components. For example:

```INF
[DefaultInstall]
include=ks.inf,kscaptur.inf
needs=[Your driver's DDInstall section],KS.Registration,KSCAPTUR.Registration.NT
```

### **Which COM Interface KsProxy Should Expose**

In the **AddReg** section of your driver's INF file, specify one of the following three GUIDs to indicate the COM interface that the KsProxy plug-in (*encapi.dll*) should expose to clients. The COM interface is determined by the property support you implemented in the encoder filter:

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th>Interface GUID</th>
<th>Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>{B43C4EEC-8C32-4791-9102-508ADA5EE8E7}</p></td>
<td><p><strong>CLSID_IVideoEncoderProxy</strong></p></td>
<td><p>Specify this GUID to cause KsProxy to expose the <strong>IVideoEncoder</strong> COM interface (for backward compatibility with the older generation of encoder support provided by Microsoft). Clients must derive this interface from the <strong>IEncoderAPI</strong> COM interface.</p></td>
</tr>
<tr class="even">
<td><p>{7FF0997A-1999-4286-A73C-622B8814E7EB}</p></td>
<td><p><strong>CLSID_ICodecAPIProxy</strong></p></td>
<td><p>Specify this GUID to cause KsProxy to expose the <strong>ICodecAPI</strong> COM interface (for non-video encoding devices such as audio-only encoders).</p></td>
</tr>
<tr class="odd">
<td><p>{B05DABD9-56E5-4FDC-AFA4-8A47E91F1C9C}</p></td>
<td><p><strong>CLSID_IVideoEncoderCodecAPIProxy</strong></p></td>
<td><p>Specify this GUID to cause KsProxy to expose both the <strong>IVideoEncoder</strong> and <strong>ICodecAPI</strong> COM interfaces (for backward and forward compatibility).</p></td>
</tr>
</tbody>
</table>

 

For example:

```INF
[Your driver's AddReg section]
HKR,Interfaces\{B43C4EEC-8C32-4791-9102-508ADA5EE8E7},,,
```

This would cause KsProxy to expose only the **IVideoEncoder** (**CLSID\_IVideoEncoderProxy**) COM interface.

These COM interfaces are documented in the DirectShow section of the DirectX 9 and Windows SDKs for Windows XP with SP1 and later.

### <a href="" id="metadata-values-that-advertise-the-encoder-filter-s-capabilities"></a>**Metadata Values That Advertise the Encoder Filter's Capabilities**

You can specify metadata values in the *Device Parameters\\Capabilities* area of the registry in the encoder's INF file. Applications can use these metadata values to determine what functionality to implement or expose to the user.

For example:

```INF
[Your driver's AddReg section]
HKR,Capabilities,,,
HKR,Capabilities,"{12345678-1234-1234-1234-12345678abcd}",,guid1
```

This would create a metadata item "{12345678-1234-1234-1234-12345678abcd} = guid1" in the *Device Parameters\\Capabilities* area of the encoder's registry settings. The empty line is necessary to create the registry key if it does not already exist.

An encoder filter may specify such static metadata in its INF file for use by applications. For example, Windows XP Media Center Edition checks for encoders that indicate that they are Windows XP Media Center Edition-compliant.

### <a href="" id="the-filter-s-kernel-streaming-category"></a>**The Filter's Kernel Streaming Category**

Kernel streaming filters must specify the kernel streaming category to which they belong. Microsoft defines GUIDs for common categories, including encoder filters and multiplexer (mux) filters.

Filters indicate their respective categories by specifying one or more of the following GUIDs in an **AddInterface** directive of the filter's section of its minidriver's INF file:

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th>Kernel streaming category GUID</th>
<th>Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>{19689BF6-C384-48FD-AD51-90E58C79F70B}</p></td>
<td><p>KSCATEGORY_ENCODER</p></td>
<td><p>Specify this GUID for encoder filters.</p></td>
</tr>
<tr class="even">
<td><p>{7A5DE1D3-01A1-452C-B481-4FA2B96271E8}</p></td>
<td><p>KSCATEGORY_MULTIPLEXER</p></td>
<td><p>Specify this GUID for mux filters.</p></td>
</tr>
</tbody>
</table>

 

To register an encoder filter, specify the KSCATEGORY\_ENCODER GUID in your driver's *DDInstall*.**Interface** INF file section. For example:

```INF
[Your Driver's DDInstall.Interface section]
AddInterface=%KSCATEGORY_ENCODER%,%KSNAME_Filter%,MyEncoderDevice.AddInterface

[MyEncoderDevice.AddInterface]
AddReg=MyEncoderDevice.AddReg

[MyEncoderDevice.AddReg]
HKR,,CLSID,,%KSProxy.CLSID%
HKR,,FriendlyName,,%MyEncoderDeviceFriendlyName%

[Strings]
KSCATEGORY_ENCODER="{19689BF6-C384-48FD-AD51-90E58C79F70B}"
KSNAME_Filter="{9B365890-165F-11D0-A195-0020AFD156E4}"
KSProxy.CLSID="17CCA71B-ECD7-11D0-B908-00A0C9223196"
MyEncoderDeviceFriendlyName="My Encoder Device"
```

**Note:** The GUID specified for *KSNAME\_Filter* must match the **ReferenceGuid** member you specified in the [**KSFILTER\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff562553) structure that describes your filter.

 

 




