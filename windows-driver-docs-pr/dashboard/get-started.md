---
title: Get Started
description: Get Started
MS-HAID:
- 'p\_dashboard.get\_started'
- 'hw\_dashboard.get\_started'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 3a0d38b9-13e2-40e5-87cb-4d057975930d
---

# Get Started


You can help your customers identify quality products that run reliably on Windows-based computers by testing your products and participating in the Windows Hardware Compatibility Program (for Windows 10), or the Windows Hardware Certification Program (for Windows 8/8.1 and older operating systems).

These programs enable you to design, create, and test your product before you submit the final version through the Windows Hardware Dev Center dashboard. The dashboard supports hardware, Windows Store app, and desktop app development, and it replaces the Windows Quality Online Services (Winqual).

**Note**  
This guide assumes the following:

-   Your company is registered with the dashboard.

    If it isn't, ask your administrator to follow the instructions in [Establish a new company](https://msdn.microsoft.com/library/windows/hardware/br230795.aspx).

-   Your company has a code signing certificate that can be used to sign submitted packages.

    If your company doesn't have a code signing certificate, or if you haven't signed your packages, ask your administrator to follow the instructions in [Update a code signing certificate](https://msdn.microsoft.com/library/windows/hardware/br230783.aspx).

-   You have a Microsoft account for the dashboard that's associated with your company.

 

## <span id="Submitting_your_products_for_the_compatibility_program_or_certification"></span><span id="submitting_your_products_for_the_compatibility_program_or_certification"></span><span id="SUBMITTING_YOUR_PRODUCTS_FOR_THE_COMPATIBILITY_PROGRAM_OR_CERTIFICATION"></span>Submitting your products for the compatibility program or certification


After you've developed and tested your product, [create a submission package](https://msdn.microsoft.com/library/windows/hardware/dn914998) and sign it by using [SignTool](http://go.microsoft.com/fwlink/p/?LinkId=238330). The signed package is what you’ll upload to the dashboard. For more information about signing your package, see [Update a code signing certificate](https://msdn.microsoft.com/library/windows/hardware/br230783.aspx).

The path that you take depends on the type of package that you're submitting.

**To submit a package**

-   Review and follow the certification process for the type of package that you want to submit:

    <table>
    <colgroup>
    <col width="50%" />
    <col width="50%" />
    </colgroup>
    <thead>
    <tr class="header">
    <th>Package type</th>
    <th>Process</th>
    </tr>
    </thead>
    <tbody>
    <tr class="odd">
    <td><p><strong>Hardware only</strong> - Drivers for a hardware device.</p></td>
    <td><ol>
    <li><p>[Create a New Hardware Certification Submission](https://msdn.microsoft.com/library/windows/hardware/hh973603.aspx)</p></li>
    <li><p>[Manage Hardware Submissions](https://msdn.microsoft.com/library/windows/hardware/br230784.aspx)</p></li>
    </ol></td>
    </tr>
    <tr class="even">
    <td><p><strong>Hardware with added software</strong> - Drivers for a hardware device, as well as additional software. For example, a digital camera that includes a photo management or editing program.</p>
    <div class="alert">
    <strong>Note</strong>  
    <p>The software must be certified before it's added to the package. The complete package must then be submitted for certification.</p>
    </div>
    <div>
     
    </div></td>
    <td><ol>
    <li><p>[Certify a New App](https://msdn.microsoft.com/library/windows/hardware/br230771.aspx)</p></li>
    <li><p>Add the software submission to your hardware submission package. For more information, see [Hardware Certification Submissions](https://msdn.microsoft.com/library/windows/hardware/br230796.aspx).</p></li>
    <li><p>[Create a New Hardware Certification Submission](https://msdn.microsoft.com/library/windows/hardware/hh973603.aspx)</p></li>
    <li><p>[Manage Hardware Submissions](https://msdn.microsoft.com/library/windows/hardware/br230784.aspx)</p></li>
    </ol></td>
    </tr>
    <tr class="odd">
    <td><p><strong>Software only</strong> - App submission.</p></td>
    <td><ol>
    <li><p>[Certify a New App](https://msdn.microsoft.com/library/windows/hardware/br230771.aspx)</p></li>
    <li><p>[Manage App Certifications](https://msdn.microsoft.com/library/windows/hardware/br230791.aspx)</p></li>
    </ol></td>
    </tr>
    <tr class="even">
    <td><p><strong>Software devices or software with a kernel-mode driver</strong> - Software with additional kernel-mode drivers, such as antimalware software that includes filter drivers.</p>
    <div class="alert">
    <strong>Note</strong>  
    <p>The drivers must be certified before they're added to the package. The complete package must then be submitted for certification.</p>
    </div>
    <div>
     
    </div></td>
    <td><ol>
    <li><p>[Create a New Hardware Certification Submission](https://msdn.microsoft.com/library/windows/hardware/hh973603.aspx)</p></li>
    <li><p>Add the hardware submission to your software submission package. For more information, see [Hardware Certification Submissions](https://msdn.microsoft.com/library/windows/hardware/br230796.aspx).</p></li>
    <li><p>[Certify a New App](https://msdn.microsoft.com/library/windows/hardware/br230771.aspx)</p></li>
    <li><p>[Manage App Certifications](https://msdn.microsoft.com/library/windows/hardware/br230791.aspx)</p></li>
    </ol></td>
    </tr>
    </tbody>
    </table>

     

After your product passes the review, it becomes eligible for the hardware compatibility or certification program. In addition, you can publish it to the **Windows Server Catalog**, the [Windows Certified Products List](https://sysdev.microsoft.com/en-US/Hardware/lpl/), and CNET.com during the submission process, or later on. You can also distribute your submitted drivers automatically during the submission process, or manually with the [Driver Distribution](https://msdn.microsoft.com/library/windows/hardware/br230778.aspx) feature.

### <span id="After_you_ve_submitted_your_product"></span><span id="after_you_ve_submitted_your_product"></span><span id="AFTER_YOU_VE_SUBMITTED_YOUR_PRODUCT"></span>After you've submitted your product

The dashboard offers the following services after you submit a product.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Service</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Reports</p></td>
<td><p>Go to the <strong>Reports</strong> page to get regularly updated information about the performance of your device.</p>
<p>If your users are having problems, you can create updates and post instructions for them.</p></td>
</tr>
<tr class="even">
<td><p>Driver distribution</p></td>
<td><p>Go to the <strong>Driver distribution</strong> page to add or update drivers for your device.</p></td>
</tr>
<tr class="odd">
<td><p>Device metadata</p></td>
<td><p>Go to the <strong>Device metadata</strong> page to add or update any images or other metadata for your device.</p></td>
</tr>
</tbody>
</table>

 

## <span id="related_topics"></span>Related topics


[Hardware Certification Submissions](https://msdn.microsoft.com/library/windows/hardware/br230796.aspx)

[Reports](https://msdn.microsoft.com/library/windows/hardware/br230776.aspx)

[Driver Distribution](https://msdn.microsoft.com/library/windows/hardware/br230778.aspx)

[Device Metadata](https://msdn.microsoft.com/library/windows/hardware/br230800.aspx)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bhw_dashboard\hw_dashboard%5D:%20Get%20Started%20%20RELEASE:%20%281/3/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





