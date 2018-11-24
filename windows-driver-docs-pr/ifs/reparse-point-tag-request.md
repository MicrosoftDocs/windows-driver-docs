---
title: Reparse Point Tag Request
description: This is the mechanism to obtain a Reparse Point tag, for those file system filter drivers that need one.
ms.assetid: B4E4382B-4FB8-4E21-8FC4-EDDE8DD4AC77
ms.date: 04/20/2017
ms.localizationpriority: medium
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

- All fields must be filled out.

- For those who do not wish to use their own name and e-mail address in this publicly-viewable database, create an e-mail address for this use (for other companies which have products that include file system/filter drivers, which have interoperability issues with yours, and need to get the test/development teams of the two companies to communicate with each other). A suggested name is *"ntifskit@YourCompanyName.com"*.

- If the "high latency" bit is enabled, this means the driver tags files and are expected to have a long latency. For example, this would be set by drivers which use Reparse Points to implement heirarchical storage solutions, etc.

- If the "name surrogate" bit is enabled, this means the driver represents another named entity in the system. For example, the name of a volume mount point or of a directory junction.

- Reparse Points are a powerful feature of Windows, but developers should be aware that there can only be one reparse point per file, and some Windows mechanisms use reparse points (HSM, Native Structured Storage). Developers need to have fallback strategies for when the reparse point tag is already in use for a file.

 

 




