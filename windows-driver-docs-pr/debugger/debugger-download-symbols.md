---
title: Download  Windows Symbol Packages for Debugging
description: This page provides downloads for Windows Symbol Packages which are used for debugging.
keywords: ["Windows Debugging Downloads", "WinDbg", "Download"]
ms.author: domars
ms.date: 02/01/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

## Download Windows Symbol Packages

![decorative image showing screen with arrow to represent download](images/download-install.png) 

Symbol files make it easier to debug your code. The easiest way to get Windows symbols is to use the [Microsoft Symbol Server](https://msdn.microsoft.com/library/windows/desktop/ee416588.aspx#using_the_microsoft_symbol_server). The symbol server makes symbols available to your debugging tools as needed. After a symbol file is downloaded from the symbol server it is cached on the local computer for quick access. Additional versions of Windows not listed here, are available on the [Microsoft Symbol Server](https://msdn.microsoft.com/library/windows/desktop/ee416588.aspx#using_the_microsoft_symbol_server). 

If you prefer to download the entire set of symbols for a particular version of Windows, download a symbol package. 

### Note on symbol package deprecation

> [!IMPORTANT]
> With the cadence that we release updates for Windows, the Windows debugging symbols we publish via the packages on this page are quickly made out of  date. 
> We have made significant improvements to the online [Microsoft Symbol Server](https://msdn.microsoft.com/library/windows/desktop/ee416588.aspx#using_the_microsoft_symbol_server) by moving this to be an Azure-based symbol store, and symbols for all Windows versions and updates are available there. 
> You can find more about this in this [MSDN blog entry](https://blogs.msdn.microsoft.com/windbg/2017/10/18/update-on-microsofts-symbol-server/). 
> Going forward we will no longer publish the offline symbol packages for RTM releases.
> 

## Symbol Package System Requirements

Before downloading and installing each symbol package, you should have at least 1 GB of disk space free, because of the size of the download package and required temporary files: 

- Each x86 symbol package may require 750 MB or more of hard disk space. 
- Each x64 symbol package may require 640 MB or more. 
- Symbol packages are non-cumulative unless otherwise noted, so if you are using an SP2 Windows release, you will need to install the symbols for the original RTM version and for SP1 before you install the symbols for SP2. 

The symbol download packages are listed by processor type (x86, and x64) and build type (retail and checked). Almost all customers require the symbols for the retail version. If you are debugging a special version of Windows with extra debugging information, then you should download the symbols for the checked version. 


## Symbol Resources and Feedback

To learn more about using symbols and debugging, see [Symbols and Symbol Files](https://docs.microsoft.com/windows-hardware/drivers/debugger/symbols-and-symbol-files). 

For help with debugging issues, see [Debugging Resources](https://docs.microsoft.com/windows-hardware/drivers/debugger/debugging-resources). 

For information on how to retrieve symbols for a machine that is not connected to the Internet, see [Using a Manifest File with SymChk](https://docs.microsoft.com/windows-hardware/drivers/debugger/using-a-manifest-file-with-symchk). 

We are interested in your feedback about symbols. Please mail suggestions or bug reports to [windbgfb@microsoft.com](mailto:windbgfb@microsoft.com). Technical support is not available from this address, but your feedback will help us to plan future changes for symbols and will make them more useful to you in the future. 


<section class="section remove-header-rule">
                        <header class="section-header">
                            <h2 id="Download_windows">Download Windows Symbol Packages</h2>
                        </header>
                        <div class="section-body">
                            <div class="spacer-32-top">
                                <div class="col-xs-24 row spacer-32-top">
                                    <section class="section remove-header-rule spacer-32-bottom">
                                        <header class="section-header">
                                        </header>
                                        <div class="section-body collapse" id="win10-1709-toggle">
                                            <section class="section item-section">
                                                <header class="section-header">
                                                    <h4 class="section-title">Windows&nbsp;10 and Windows Server, version 1709 symbols – October 2017</h4>
                                                </header>
                                                <div class="section-body">
                                                    <p>
                                                        The packages released in October 2017 contain the full set of symbols required to debug the following: Windows&nbsp;10, Windows&nbsp;10 Enterprise, Windows Server Standard, version 1709, and Windows Server Datacenter, version 1709.
                                                    </p>
                                                    <ul class="bulleted-list">
                                                        <li>
                                                            <a href="http://download.microsoft.com/download/5/C/9/5C911080-15B0-4829-9D62-E65FC6F16301/Windows_RS3.16299.15.170928-1534.x64FRE.Symbols.msi">Windows&nbsp;10, x64 retail symbols</a>
                                                        </li>
                                                        <li>
                                                            <a href="http://download.microsoft.com/download/5/C/9/5C911080-15B0-4829-9D62-E65FC6F16301/Windows_RS3.16299.15.170928-1534.X86FRE.Symbols.msi">Windows&nbsp;10, x86 32-bit retail symbols</a>
                                                        </li>
                                                    </ul>
                                                </div>
                                            </section>
                                        </div>
                                    </section>
                                    <section class="section remove-header-rule spacer-32-bottom">
                                        <header class="section-header">
                                        </header>
                                        <div class="section-body collapse" id="win10-2017-4-toggle">
                                            <section class="section item-section">
                                                <header class="section-header">
                                                    <h4 class="section-title">Windows&nbsp;10, version 1703 and Windows Server 2016 symbols – April 2017 </h4>
                                                </header>
                                                <div class="section-body">
                                                    <p>
                                                        The packages released in April of 2017 contain the full set of symbols required to debug the following: Windows&nbsp;10, Windows&nbsp;10 Enterprise, Windows Server 2016, Standard, Windows Server 2016 Datacenter, Windows Storage Server 2016 Workgroup, Windows Storage Server 2016 Standard, Windows Server 2016 Essentials, and Microsoft Hyper-V Server 2016. 
                                                    </p>
                                                    <ul class="bulleted-list">
                                                        <li>
                                                            <a href="//download.microsoft.com/download/6/9/C/69C86A1F-C8E9-4F28-B6FC-9FA2BCE98BC0/Windows_Rs2.15063.0.170317-1834.x64FRE.Symbols.msi">Windows&nbsp;10, x64 retail symbols</a>
                                                        </li>
                                                        <li>
                                                            <a href="//download.microsoft.com/download/6/9/C/69C86A1F-C8E9-4F28-B6FC-9FA2BCE98BC0/Windows_Rs2.15063.0.170317-1834.X86FRE.Symbols.msi">Windows&nbsp;10, x86 32-bit retail symbols</a>
                                                        </li>
                                                    </ul>
                                                </div>
                                            </section>
                                        </div>
                                    </section>
                                    <section class="section remove-header-rule spacer-32-bottom">
                                        <header class="section-header">
                                        </header>
                                        <div class="section-body collapse" id="win10-2016-9-toggle">
                                            <section class="section item-section">
                                                <header class="section-header">
                                                    <h4 class="section-title">Windows&nbsp;10 preview symbols - September 2016 </h4>
                                                </header>
                                                <div class="section-body">
                                                    <p>
                                                        The packages released September 2016, contain the preview symbols required to debug Windows&nbsp;10 and Windows&nbsp;10 Enterprise.  These are preview symbols that should be used with the pre-release or flighted builds of Windows&nbsp;10.
                                                    </p>
                                                    <ul class="bulleted-list">
                                                        <li>
                                                            <a href="//download.microsoft.com/download/1/7/8/17859C19-BD31-42F9-A669-3C7516BA3B12/Windows_Rs.14915.1000.160826-1902.x64FRE.Symbols.msi">Windows&nbsp;10, x64 retail symbols</a>
                                                        </li>
                                                        <li>
                                                            <a href="//download.microsoft.com/download/1/7/8/17859C19-BD31-42F9-A669-3C7516BA3B12/Windows_Rs.14915.1000.160826-1902.X86FRE.Symbols.msi">Windows&nbsp;10, x86 32-bit retail symbols</a>
                                                        </li>
                                                    </ul>
                                                </div>
                                            </section>
                                        </div>
                                    </section>
                                    <section class="section remove-header-rule spacer-32-bottom">
                                        <header class="section-header">
                                        </header>
                                        <div class="section-body collapse" id="win10-2016-8-toggle">
                                            <section class="section item-section">
                                                <header class="section-header">
                                                    <h4 class="section-title">Windows&nbsp;10, version 1607 and Windows Server 2016 Symbols - August 2016</h4>
                                                </header>
                                                <div class="section-body">
                                                    <p>
                                                        The packages released August 2016, contain the full set of symbols required to debug Windows&nbsp;10, Windows&nbsp;10 Enterprise, Windows Server 2016, Standard, Windows Server 2016 Datacenter, Windows Storage Server 2016 Workgroup, Windows Storage Server 2016 Standard, Windows Server 2016 Essentials, Microsoft Hyper-V Server 2016.
                                                    </p>
                                                    <ul class="bulleted-list">
                                                        <li>
                                                            <a href="//download.microsoft.com/download/D/1/9/D196C4F3-FC5B-48D2-A5D9-D3D42CE5F4F0/Windows_Rs1.14393.0.160715-1616.x64FRE.Symbols.msi">Windows&nbsp;10, x64 retail symbols</a>
                                                        </li>
                                                        <li>
                                                            <a href="//download.microsoft.com/download/D/1/9/D196C4F3-FC5B-48D2-A5D9-D3D42CE5F4F0/Windows_Rs1.14393.0.160715-1616.X86FRE.Symbols.msi">Windows&nbsp;10, x86 32-bit retail symbols</a>
                                                        </li>
                                                    </ul>
                                                </div>
                                            </section>
                                        </div>
                                    </section>
                                    <section class="section remove-header-rule spacer-32-bottom">
                                        <header class="section-header">
                                        </header>
                                        <div class="section-body collapse" id="win10-0-toggle">
                                            <section class="section item-section">
                                                <header class="section-header">
                                                    <h4 class="section-title">Windows&nbsp;10 Insider Preview Build 14295  – March 2016 </h4>
                                                </header>
                                                <div class="section-body">
                                                    <p>
                                                        The packages released March 2016, contain the full set of symbols required to debug Windows&nbsp;10 Insider Preview Build 14295.
                                                    </p>
                                                    <ul class="bulleted-list">
                                                        <li>
                                                            <a href="//download.microsoft.com/download/0/F/9/0F9FBD64-AACA-4152-BCC1-6C7D6FD64A19/Windows_Rs1.14295.1000.160318-1628.x64FRE.Symbols.msi">Windows&nbsp;10, x64 retail symbols</a>
                                                        </li>
                                                        <li>
                                                            <a href="//download.microsoft.com/download/0/F/9/0F9FBD64-AACA-4152-BCC1-6C7D6FD64A19/Windows_Rs1.14295.1000.160318-1628.X86FRE.Symbols.msi">Windows&nbsp;10, x86 32-bit retail symbols</a>
                                                        </li>
                                                    </ul>
                                                </div>
                                            </section>
                                        </div>
                                    </section>
                                    <section class="section remove-header-rule spacer-32-bottom">
                                        <header class="section-header">
                                        </header>
                                        <div class="section-body collapse" id="win10-toggle">
                                            <section class="section item-section">
                                                <header class="section-header">
                                                    <h4 class="section-title">Windows&nbsp;10, Version 1511 Symbols – November 2015</h4>
                                                </header>
                                                <div class="section-body">
                                                    <p>
                                                        The packages released November 2015, contain the full set of symbols required to debug Windows&nbsp;10, Windows&nbsp;10 Enterprise, Windows Server Technical Preview, Windows Datacenter Technical Preview, and Windows Hyper-V Server Technical Preview.
                                                    </p>
                                                    <ul class="bulleted-list">
                                                        <li>
                                                            <a href="//download.microsoft.com/download/B/9/0/B90E8A27-A45C-499B-931E-D908F8CB84F1/Windows_Th2.10586.0.151029-1700.x64FRE.Symbols.msi">Windows&nbsp;10, x64 retail symbols</a>
                                                        </li>
                                                        <li>
                                                            <a href="//download.microsoft.com/download/B/9/0/B90E8A27-A45C-499B-931E-D908F8CB84F1/Windows_Th2.10586.0.151029-1700.x64CHK.Symbols.msi">Windows&nbsp;10, x64 checked symbols</a>
                                                        </li>
                                                        <li>
                                                            <a href="//download.microsoft.com/download/B/9/0/B90E8A27-A45C-499B-931E-D908F8CB84F1/Windows_Th2.10586.0.151029-1700.X86FRE.Symbols.msi">Windows&nbsp;10, x86 32-bit retail symbols</a>
                                                        </li>
                                                        <li>
                                                            <a href="//download.microsoft.com/download/B/9/0/B90E8A27-A45C-499B-931E-D908F8CB84F1/Windows_Th2.10586.0.151029-1700.X86CHK.Symbols.msi">Windows&nbsp;10, x86 32-bit checked symbols</a>
                                                        </li>
                                                    </ul>
                                                </div>
                                            </section>
                                        </div>
                                    </section>
                                    <section class="section remove-header-rule spacer-32-bottom">
                                        <header class="section-header">
                                        </header>
                                        <div class="section-body collapse" id="win10-1-toggle">
                                            <section class="section item-section">
                                                <header class="section-header">
                                                    <h4 class="section-title">Windows&nbsp;10 Symbols – July 2015 </h4>
                                                </header>
                                                <div class="section-body">
                                                    <p>
                                                        These packages contain the full set of symbols required to debug Windows&nbsp;10, Windows&nbsp;10 for Enterprise, Windows Server Technical Preview, Windows Datacenter Technical Preview, and Windows Hyper-V Server Technical Preview, released July 29, 2015.
                                                    </p>
                                                    <ul class="bulleted-list">
                                                        <li>
                                                            <a href="//download.microsoft.com/download/C/F/F/CFFED264-98B4-40C5-8A9E-9C1659E01092/Windows_TH1.10240.16384.150709-1700.x64FRE.Symbols.msi">Windows&nbsp;10, x64 retail symbols</a>
                                                        </li>
                                                        <li>
                                                            <a href="//download.microsoft.com/download/C/F/F/CFFED264-98B4-40C5-8A9E-9C1659E01092/Windows_TH1.10240.16384.150709-1700.x64CHK.Symbols.msi">Windows&nbsp;10, x64 checked symbols</a>
                                                        </li>
                                                        <li>
                                                            <a href="//download.microsoft.com/download/C/F/F/CFFED264-98B4-40C5-8A9E-9C1659E01092/Windows_TH1.10240.16384.150709-1700.X86FRE.Symbols.msi">Windows&nbsp;10, x86 32-bit retail symbols</a>
                                                        </li>
                                                        <li>
                                                            <a href="//download.microsoft.com/download/C/F/F/CFFED264-98B4-40C5-8A9E-9C1659E01092/Windows_TH1.10240.16384.150709-1700.X86CHK.Symbols.msi">Windows&nbsp;10, x86 32-bit checked symbols</a>
                                                        </li>
                                                    </ul>
                                                </div>
                                            </section>
                                        </div>
                                    </section>

<section class="section remove-header-rule spacer-32-bottom">
                                        <header class="section-header">
                                        </header>
                                        <div class="section-body collapse" id="win8-toggle">
                                            <section class="section item-section">
                                                <header class="section-header">
                                                    <h4 class="section-title">Windows RT 8.1 ARM, Windows&nbsp;8.1 and Windows Server 2012 R2 Symbols</h4>
                                                </header>
                                                <div class="section-body">
                                                    <p>
                                                        These packages contain the full set of symbols required to debug Windows RT 8.1 ARM, Windows&nbsp;8.1 and Windows Server 2012 R2, released October 17, 2013.
                                                    </p>
                                                    <ul class="bulleted-list">
                                                        <li>
                                                            <a href="//download.microsoft.com/download/D/1/A/D1AD0063-7ECE-4589-A846-4971B56AFF09/Windows_winblue.9600.16384.130821-1623.woachk.Symbols-IRM_SYM_WOACHK_EN-US_MSI.msi">Windows RT 8.1 ARM checked symbols</a>
                                                        </li>
                                                        <li>
                                                            <a href="//download.microsoft.com/download/D/1/A/D1AD0063-7ECE-4589-A846-4971B56AFF09/Windows_winblue.9600.16384.130821-1623.woafre.Symbols-IRM_SYM_WOAFRE_EN-US_MSI.msi">Windows RT 8.1 ARM retail symbols</a>
                                                        </li>
                                                        <li>
                                                            <a href="//download.microsoft.com/download/D/1/A/D1AD0063-7ECE-4589-A846-4971B56AFF09/Windows_winblue.9600.16384.130821-1623.x64chk.Symbols-IRM_SYM_X64CHK_EN-US_MSI.msi">Windows&nbsp;8.1 and Windows Server 2012 R2, x64 checked symbols</a>
                                                        </li>
                                                        <li>
                                                            <a href="//download.microsoft.com/download/D/1/A/D1AD0063-7ECE-4589-A846-4971B56AFF09/Windows_winblue.9600.16384.130821-1623.x64fre.Symbols-IRM_SYM_X64FRE_EN-US_MSI.msi">Windows&nbsp;8.1 and Windows Server 2012 R2, x64 retail symbols</a>
                                                        </li>
                                                        <li>
                                                            <a href="//download.microsoft.com/download/D/1/A/D1AD0063-7ECE-4589-A846-4971B56AFF09/Windows_winblue.9600.16384.130821-1623.x86chk.Symbols-IRM_SYM_X86CHK_EN-US_MSI.msi">Windows&nbsp;8.1 x86 32-bit checked symbols</a>
                                                        </li>
                                                        <li>
                                                            <a href="//download.microsoft.com/download/D/1/A/D1AD0063-7ECE-4589-A846-4971B56AFF09/Windows_winblue.9600.16384.130821-1623.x86fre.Symbols-IRM_SYM_X86FRE_EN-US_MSI.msi">Windows&nbsp;8.1 x86 32-bit retail symbols</a>
                                                        </li>
                                                    </ul>
                                                </div>
                                            </section>                                 
                                        </div>
 </section>
<section class="section remove-header-rule spacer-32-bottom">
                                        <header class="section-header">
                                        </header>
                                        <div class="section-body collapse" id="win8-2-toggle">
                                            <section class="section item-section">
                                                <header class="section-header">
                                                    <h4 class="section-title">Windows&nbsp;8 and Windows Server 2012 Symbols</h4>
                                                </header>
                                                <div class="section-body">
                                                    <p>
                                                        These packages contain the full set of symbols required to debug Windows&nbsp;8 and Windows Server 2012, released August 15, 2012.
                                                    </p>
                                                    <ul class="bulleted-list">
                                                        <li>
                                                            <a href="//download.microsoft.com/download/D/6/A/D6A258F4-11DA-479A-8A30-F9EB0B2951F9/Windows_Win8.9200.16384.120725-1247.X86FRE.Symbols.msi">Windows&nbsp;8 RTM x86 32-bit retail symbols</a>
                                                        </li>
                                                        <li>
                                                            <a href="//download.microsoft.com/download/D/6/A/D6A258F4-11DA-479A-8A30-F9EB0B2951F9/Windows_Win8.9200.16384.120725-1247.X86CHK.Symbols.msi">Windows&nbsp;8 RTM x86 32-bit checked symbols</a>
                                                        </li>
                                                        <li>
                                                            <a href="//download.microsoft.com/download/D/1/7/D17C7B6B-D0A0-4918-9B83-82024D2EC9D2/Windows_Win8.9200.16384.120725-1247.x64FRE.Symbols.msi">Windows&nbsp;8 RTM, x64 retail symbols</a>
                                                        </li>
                                                        <li>
                                                            <a href="//download.microsoft.com/download/D/1/7/D17C7B6B-D0A0-4918-9B83-82024D2EC9D2/Windows_Win8.9200.16384.120725-1247.x64CHK.Symbols.msi">Windows&nbsp;8 RTM, x64 checked symbols</a>
                                                        </li>
                                                    </ul>
                                                </div>
                                            </section>        
                                        </div>
</section>

<section class="section remove-header-rule spacer-32-bottom">
                                        <header class="section-header">
                                        </header>
                                        <div class="section-body collapse" id="win7-toggle">
                                            <section class="section item-section">
                                                <header class="section-header">
                                                    <h4 class="section-title">Windows&nbsp;7 Service Pack 1 Symbols</h4>
                                                </header>
                                                <div class="section-body">
                                                    <p>
                                                        These packages contain the full set of symbols required to debug the Windows&nbsp;7 Service Pack 1.
                                                    </p>
                                                    <p>
                                                        <strong>Note:</strong> These packages also contain the full set of symbols required to debug Windows Server 2008 R2 Service Pack 1.
                                                    </p>
                                                    <ul class="bulleted-list">
                                                        <li>
                                                            <a href="//download.microsoft.com/download/0/A/F/0AFB5316-3062-494A-AB78-7FB0D4461357/Windows_Win7SP1.7601.17514.101119-1850.X86FRE.Symbols.msi">Windows&nbsp;7 Service Pack 1 x86 retail symbols, all languages</a> (File size: 330 MB - Most customers want this package.)
                                                        </li>
                                                        <li>
                                                            <a href="//download.microsoft.com/download/0/A/F/0AFB5316-3062-494A-AB78-7FB0D4461357/Windows_Win7SP1.7601.17514.101119-1850.X86CHK.Symbols.msi">Windows&nbsp;7 Service Pack 1 x86 checked symbols, all languages</a> (File size: 294 MB)
                                                        </li>
                                                        <li>
                                                            <a href="//download.microsoft.com/download/0/A/F/0AFB5316-3062-494A-AB78-7FB0D4461357/Windows_Win7SP1.7601.17514.101119-1850.AMD64FRE.Symbols.msi">Windows&nbsp;7 Service Pack 1 x64 retail symbols, all languages</a> (File size: 287 MB)
                                                        </li>
                                                        <li>
                                                            <a href="//download.microsoft.com/download/0/A/F/0AFB5316-3062-494A-AB78-7FB0D4461357/Windows_Win7SP1.7601.17514.101119-1850.AMD64CHK.Symbols.msi">Windows&nbsp;7 Service Pack 1 x64 checked symbols, all languages</a> (File size: 262 MB)
                                                        </li>
                                                    </ul>
                                                </div>
</section>

<section class="section item-section">
                                                <header class="section-header">
                                                    <h4 class="section-title">Windows&nbsp;7 RTM Symbols</h4>
                                                </header>
                                                <div class="section-body">
                                                    <p>
                                                        These packages contain the full set of symbols required to debug the Windows&nbsp;7 RTM.
                                                    </p>
                                                    <p>
                                                        <b>Note:</b> These packages also contain the full set of symbols required to debug Windows Server 2008 R2 RTM.
                                                    </p>
                                                    <ul class="bulleted-list">
                                                        <li>
                                                            <a href="//download.microsoft.com/download/7/F/B/7FBF7E6A-D0DE-442A-A683-4F9885A96FC9/Windows_Win7.7600.16385.090713-1255.X86FRE.Symbols.msi">Windows&nbsp;7 RTM x86 retail symbols, all languages</a> (File size: 323 MB - Most customers want this package.)
                                                        </li>
                                                        <li>
                                                            <a href="//download.microsoft.com/download/7/F/B/7FBF7E6A-D0DE-442A-A683-4F9885A96FC9/Windows_Win7.7600.16385.090713-1255.X86CHK.Symbols.msi">Windows&nbsp;7 RTM x86 checked symbols, all languages</a> (File size: 288 MB)
                                                        </li>
                                                        <li>
                                                            <a href="//download.microsoft.com/download/F/1/1/F11206A1-C532-4C9E-86FF-1261A693AA53/Windows_Win7.7600.16385.090713-1255.X64FRE.Symbols.msi">Windows&nbsp;7 RTM x64 retail symbols, all languages</a> (File size: 286 MB)
                                                        </li>
                                                        <li>
                                                            <a href="//download.microsoft.com/download/F/1/1/F11206A1-C532-4C9E-86FF-1261A693AA53/Windows_Win7.7600.16385.090713-1255.X64CHK.Symbols.msi">Windows&nbsp;7 RTM x64 checked symbols, all languages</a> (File size: 260 MB)
                                                        </li>
                                                    </ul>
                                                </div>
</section>




# Looking for related downloads?
-------------------

[Download Windows Debugging Tools](debugger-download-tools.md) 

[Download the Windows Driver Kit (WDK)](https://developer.microsoft.com/windows/hardware/windows-driver-kit) 

[Download the Windows Assessment and Deployment Kit (Windows ADK)](https://developer.microsoft.com/windows/hardware/windows-assessment-deployment-kit) 

[Download the Windows HLK, HCK, or Logo Kit](https://developer.microsoft.com/windows/hardware/windows-hardware-lab-kit) 

[Download Windows Insider Preview builds](https://insider.windows.com/) 
 


[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!debugger-download%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




