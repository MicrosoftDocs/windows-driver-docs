---
title: Debugger Downloads
description: This page provides downloads for the Windows Debugging tools, such as WinDbg.
keywords: ["Windows Debugging Downloads", "WinDbg", "Download"]
ms.author: domars
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# ![decorative image showing screen with arrow to represent download](images/download-install.png) Download Debugging tools for Windows


The Windows Debugger (WinDbg) can be used to debug kernel and user mode code, analyze crash dumps and to examine the CPU registers as code executes. 


## WinDbg Preview  
 

WinDbg Preview is a new version of WinDbg with more modern visuals, faster windows, a full-fledged scripting experience, built with the extensible debugger data model front and center. WinDbg Preview is using the same underlying engine as WinDbg today, so all the commands, extensions, and workflows still work as they did before. 

Download WinDbg Preview from the Microsoft Store 

Learn more about installation and configuration  


## Debugging Tools for Windows 10 (WinDbg) 

If you just need the Debugging Tools for Windows 10, and not WDK 10 or Visual Studio 2017, you can install the debugging tools as a standalone component from Windows SDK. In the installation wizard, select *Debugging Tools for Windows*, and deselect all other components. 

Get Debugging Tools for Windows (WinDbg) (from the SDK) 

Learn more about WinDbg and other debuggers (WinDbg, KD, CDB, NTSD) 


# ![decorative image showing screen with arrow to represent download](images/download-install.png)  Download Windows Symbol Packages

Symbol files make it easier to debug your code. The easiest way to get Windows symbols is to use the [Microsoft Symbol Server](https://msdn.microsoft.com/library/windows/desktop/ee416588.aspx#using_the_microsoft_symbol_server). If you prefer to download the entire set of symbols for a particular version of Windows, download a symbol package. 

## Note on symbol package deprecation

>![IMPORTANT]
> With the cadence that we release updates for Windows, the Windows debugging symbols we publish via the packages on this page are quickly made out of date. We have made significant improvements to the online [Microsoft Symbol Server](https://msdn.microsoft.com/library/windows/desktop/ee416588.aspx#using_the_microsoft_symbol_server) by moving this to be an Azure-based symbol store, and symbols for all Windows versions and updates are available there. You can find more about this in this [MSDN blog entry](https://blogs.msdn.microsoft.com/windbg/2017/10/18/update-on-microsofts-symbol-server/). Going forward we will no longer publish the offline symbol packages for RTM releases. 


## Get Windows Symbol Packages 


The easiest way to get Windows symbols is to use the [Microsoft Symbol Server](https://msdn.microsoft.com/library/windows/desktop/ee416588.aspx#using_the_microsoft_symbol_server). The symbol server makes symbols available to your debugging tools as needed. After a symbol file is downloaded from the symbol server it is cached on the local computer for quick access. Additional versions of Windows not listed here, are available on the [Microsoft Symbol Server](https://msdn.microsoft.com/library/windows/desktop/ee416588.aspx#using_the_microsoft_symbol_server). 

If you prefer to download the entire set of symbols for Windows 10, Windows 8.1, Windows Server 2012 R2, Windows 8, Windows Server 2012, or Windows 7, then you can download a symbol package and install it on your computer. 

## Symbol Package System Requirements

Before downloading and installing each symbol package, you should have at least 1 GB of disk space free, because of the size of the download package and required temporary files: 

- Each x86 symbol package may require 750 MB or more of hard disk space. 
- Each x64 symbol package may require 640 MB or more. 
- Symbol packages are non-cumulative unless otherwise noted, so if you are using an SP2 Windows release, you will need to install the symbols for the original RTM version and for SP1 before you install the symbols for SP2. 

## Symbol Package Installation Instructions
The symbol download packages are listed by processor type (x86, Itanium, and x64) and build type (retail and checked). Almost all customers require the symbols for the retail version. If you are debugging a special version of Windows with extra debugging information, then you should download the symbols for the checked version. 


## Symbol Resources, Support, and Feedback

To learn more about using symbols and debugging, see Debugging Tools for Windows. 
For help with debugging issues, see Debugging Resources. 
For information on how to retrieve symbols for a machine that is not connected to the Internet, see Using a Manifest File with SymChk. 
Feedback- We are interested in your feedback about symbols. Please mail suggestions or bug reports to windbgfb@microsoft.com. Technical support is not available from this address, but your feedback will help us to plan future changes for symbols and will make them more useful to you in the future. 

## Download Windows Symbol Packages

Windows 10 and Windows Server, version 1709 – October 2017   
Windows 10 and Windows Server 2016 – April 2017   
Windows 10 - September 2016   
Windows 10 and Windows Server 2016 - August 2016   
Windows 10 – March 2016   
Windows 10 – November 2015   
Windows 10 – July 2015   
Windows RT 8.1 ARM, Windows 8.1 and Windows Server 2012 R2   
Windows 8   


<section class="section item-section">
                                                <header class="section-header">
                                                    <h4 class="section-title">Windows&nbsp;7 RC Symbols</h4>
                                                </header>
                                                <div class="section-body">
                                                    <p>
                                                        These packages contain the full set of symbols required to debug the Windows&nbsp;7 Release Candidate (RC).
                                                    </p>
                                                    <ul class="bulleted-list">
                                                        <li>
                                                            <a href="//download.microsoft.com/download/8/B/7/8B723049-19CF-444C-9755-160FD8A4C233/Windows_Winmain.7100.0.090421-1700.X86FRE.Symbols.msi">Windows&nbsp;7 RC x86 retail symbols, all languages</a> (File size: 208 MB - Most customers want this package.)
                                                        </li>
                                                        <li>
                                                            <a href="//download.microsoft.com/download/8/B/7/8B723049-19CF-444C-9755-160FD8A4C233/Windows_Winmain.7100.0.090421-1700.X86CHK.Symbols.msi">Windows&nbsp;7 RC x86 checked symbols, all languages</a> (File size: 288 MB)
                                                        </li>
                                                        <li>
                                                            <a href="//download.microsoft.com/download/8/7/6/876ECDEA-C26F-4540-A97C-52A5A7861448/Windows_Winmain.7100.0.090421-1700.AMD64FRE.Symbols.msi">Windows&nbsp;7 RC x64 retail symbols, all languages</a> (File size: 286 MB)
                                                        </li>
                                                        <li>
                                                            <a href="//download.microsoft.com/download/8/7/6/876ECDEA-C26F-4540-A97C-52A5A7861448/Windows_Winmain.7100.0.090421-1700.AMD64CHK.Symbols.msi">Windows&nbsp;7 RC x64 checked symbols, all languages</a> (File size: 260 MB)
                                                        </li>
                                                        <li>
                                                            <a href="//download.microsoft.com/download/C/A/E/CAEA5DA9-8CD8-47B4-B0EA-B4B28DEF5F88/Windows_Winmain.7100.0.090421-1700.IA64FRE.Symbols.msi">Windows&nbsp;7 RC Itanium retail symbols, all languages</a> (File size: 192 MB)
                                                        </li>
                                                        <li>
                                                            <a href="//download.microsoft.com/download/C/A/E/CAEA5DA9-8CD8-47B4-B0EA-B4B28DEF5F88/Windows_Winmain.7100.0.090421-1700.IA64CHK.Symbols.msi">Windows&nbsp;7 RC Itanium checked symbols, all languages</a> (File size: 240 MB)
                                                        </li>
                                                    </ul>
                                                </div>
                                            </section>
                                        </div>
</section>




# Looking for related downloads?
-------------------

Download Windows Symbol Packages 
Download the Windows Driver Kit (WDK) 
Download the Windows Assessment and Deployment Kit (Windows ADK) 
Download the Windows HLK, HCK, or Logo Kit 
Download Windows Insider Preview builds 
 




[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!debugger-download%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




