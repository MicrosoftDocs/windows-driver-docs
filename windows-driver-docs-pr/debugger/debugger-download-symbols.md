---
title: Windows Symbol Packages for Debugging
description: Learn about Windows symbol packages, which are used for debugging, and how to get Windows symbols with the Microsoft public symbol server.
keywords: ["Windows Debugging Downloads", "WinDbg", "Download", "Symbols","Download Symbols"]
ms.date: 04/04/2025
ms.topic: concept-article
---

# Windows symbol packages for debugging

Symbol files make it easier to debug your code by providing data like variable names to the debugging tools. The easiest way to get Windows symbols is to use the [Microsoft public symbol server](microsoft-public-symbols.md). The symbol server makes symbols available to your debugging tools as needed. After a symbol file is downloaded from the symbol server, it's cached on the local computer for quick access.

## Symbol package deprecation

> [!IMPORTANT]
> We no longer publish the offline symbol packages for Windows.
>
> Given the frequent updates for Windows, the Windows debugging symbols that were published as packages are quickly made out of date.
> Symbols are available online through the *[Microsoft public symbol server](microsoft-public-symbols.md)*, which uses an Azure-based symbol store. Symbols for all Windows versions and updates are available there.
> You can find more information in this archived *[blog entry](/archive/blogs/windbg/update-on-microsofts-symbol-server)*.
>
> For information on how to retrieve symbols for a machine that's not connected to the Internet, see *[Using a manifest file with SymChk](using-a-manifest-file-with-symchk.md)*.

## Symbol resources and feedback

To learn more about using symbols and debugging, see [Symbols and symbol files](symbols-and-symbol-files.md).

For help with debugging issues, see [Debugging resources](debugging-resources.md).

We're interested in your feedback about symbols. Mail suggestions or bug reports to [windbgfb@microsoft.com](mailto:windbgfb@microsoft.com). Technical support isn't available from this address, but your feedback will help us to plan future changes for symbols distribution.

## See also

- [Download Windows Debugging Tools](debugger-download-tools.md)

- [Download the Windows Driver Kit (WDK)](../download-the-wdk.md)

- [Download the Windows Assessment and Deployment Kit (Windows ADK)](/windows-hardware/get-started/adk-install)

- [Download the Windows HLK, HCK, or Logo Kit](/windows-hardware/test/hlk/windows-hardware-lab-kit)

- [Download Windows Insider Preview builds](https://insider.windows.com/)
