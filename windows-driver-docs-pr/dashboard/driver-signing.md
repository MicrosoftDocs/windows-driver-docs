---
title: Driver signing
description: Driver signing
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: e0d378a7-79dd-4af8-a5b9-aa90452cc78d
---

# Driver Signing

Driver signing is a service provided by the Hardware Dev Center dashboard. This service allows you to digitally sign Windows 10 drivers with a Microsoft signature. You can also get drivers signed by completing the requirements for the Windows Hardware Compatibility Program. For more information on how basic Driver Signing is different from the Compatibility program see,[Windows Hardware Compatibility Program](http://go.microsoft.com/fwlink/p/?linkid=525487).

Driver signing submissions require an extended validation (EV) code signing certificate. For more information about code signing certificates, see [Get a code signing certificate](https://msdn.microsoft.com/windows/hardware/drivers/dashboard/update-a-code-signing-certificate).

## Submit a driver for signing
<ol>
  <li> <p>Sign in to the Hardware Dev Center dashboard with your Microsoft account, and then click **File signing services**.</p> </li>
  <li><p> On the **File signing services** page, in the **Create submissions** tile, click **Create Driver Signing submission**.
  > [!NOTE]
  > Before proceeding, you may be asked to sign a legal agreement. To continue, review the document, add your signature, add the date, and then click Submit. Each organization only needs to sign this agreement once.
  </p>
  </li>
  <li><p>
  On the Create Driver Signing submission page, complete the following information:

 | Field | Description |
 | --- | --- |
 | Name | This allows you to easily identify and find your product later. It’s also the name which will be shown on the Universal Driver List (if applicable).
 | Announcement Date |This is the date when your product will appear on the Universal Driver list (if applicable). This allows you to prevent disclosure until you’re ready.
 | Universal Driver? |  This allows you to choose whether or not the drivers in your submission are Universal. Learn more about [What’s new in Driver development](https://msdn.microsoft.com/windows/hardware/drivers/what-s-new-in-driver-development). |
  </p> </li>
  <li><p>After your submission is processed you’ll receive an email with the results.
  > [!IMPORTANT]
  > <ol type="a">
    <li> <p>All Driver Signing submissions must be in a single, signed CAB file. </p></li>
    <li><p>The CAB file signature must match the EV code signing certificate on file for your company with Windows Dev Center hardware dashboard. For more information about code signing certificates, see <a href="https://msdn.microsoft.com/windows/hardware/drivers/dashboard/update-a-code-signing-certificate">Get a code signing certificate.</p></li>
    <li><p>All driver folders in your cab must support the same set of architectures. For example, all drivers must be x86 or x64. Otherwise, all drivers must support both x86 and x64. For packages that support both x86 and x64, a single INF file supporting both architectures and binaries is required for each architectures.</p></li>
    <li><p>The CAB should not contain symbols.</p></li>
    <li><p>The CAB should not have files at the root level, and each driver package must be in separate folders. The following illustration is an example of the CAB structure.</p><img src="images/b-wes-driversigning.png" alt="an image showing a CAB structure"></img></li>
  > </ol>
  </p>

### Manage driver Submissions

1. Sign in to Hardware Dev Center dashboard with your Microsoft account, and then click **Manage submissions** in the **Hardware certification** tile.
2. On the **Manage submissions** page, select **Driver Signing** from the **Submission type** list, and then click **Apply**.
3. Click the submission ID that you want to manage.
4. On the submission details page, you can see the status of your submission. If it's complete, click the **Download** link to download the signed binaries.

## Related topics
[Update a code signing certificate](https://msdn.microsoft.com/windows/hardware/drivers/dashboard/update-a-code-signing-certificate)

[Establish a new company](https://msdn.microsoft.com/windows/hardware/drivers/dashboard/establish-a-new-company)

[Get a code signing certificate](https://msdn.microsoft.com/en-us/windows/hardware/drivers/dashboard/get-a-code-signing-certificate)

[Windows Hardware Compatibility Program](https://developer.microsoft.com/en-us/windows/hardware/compatibility-program)
