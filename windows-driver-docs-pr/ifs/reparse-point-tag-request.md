---
title: Reparse Point Tag Request
author: windows-driver-content
description: This is the mechanism to obtain a Reparse Point tag, for those file system filter drivers that need one.
ms.assetid: B4E4382B-4FB8-4E21-8FC4-EDDE8DD4AC77
---

# Reparse Point Tag Request


This is the mechanism to obtain a Reparse Point tag, for those file system filter drivers that need one.

## <span id="Reparse_Point_Tag_Request"></span><span id="reparse_point_tag_request"></span><span id="REPARSE_POINT_TAG_REQUEST"></span>Reparse Point Tag Request


To obtain a Reparse Point tag, send the following information to Microsoft.

-   Company name
-   Company e-mail
-   Company URL
-   Contact e-mail
-   Product name
-   Product URL
-   Product Description: (1 paragraph summary)
-   Driver filename
-   Driver device name
-   Driver GUID
-   High-latency bit enabled (yes/no)
-   Name surrogate bit enabled (yes/no)

Send this information in an ASCII text e-mail message to <rpid@microsoft.com>. A *ReparseID* value for this driver will then be e-mailed back to the specified contact e-mail address.

The following list details some requirements for submitting a request.

-   All fields must be filled out.

-   For those who do not wish to use their own name and e-mail address in this publicly-viewable database, create an e-mail address for this use (for other companies which have products that include file system/filter drivers, which have interoperability issues with yours, and need to get the test/development teams of the two companies to communicate with each other). A suggested name is *"ntifskit@YourCompanyName.com"*.

-   If the "high latency" bit is enabled, this means the driver tags files and are expected to have a long latency. For example, this would be set by drivers drivers which use Reparse Points to implement heirarchical storage solutions, etc.

-   If the "name surrogate" bit is enabled, this means the driver represents another named entity in the system. For example, the name of a volume mount point or of a directory junction.

-   Reparse Points are a powerful feature of Windows, but developers should be aware that there can only be one reparse point per file, and some Windows mechanisms use reparse points (HSM, Native Structured Storage). Developers need to have fallback strategies for when the reparse point tag is already in use for a file.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20Reparse%20Point%20Tag%20Request%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


