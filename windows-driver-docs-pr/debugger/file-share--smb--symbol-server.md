---
title: File share (SMB) symbol server
description: Learn how to run an SMB symbol server by creating a file share and assigning permissions to access the file share.
ms.date: 12/08/2022
---

# File share (SMB) symbol server

To run an SMB symbol server, create a file share and assign permissions to give users or groups access to the file share.

## Create an SMB file share symbol store

Use File Explorer or Computer Management to create a file share and assign permissions.

The steps in the following sections assume that the symbols are located in D:\\SymStore\\Symbols.

### File Explorer

To assign file share permissions by using File Explorer:

1. Open File Explorer.

1. Select and hold (or right-click) the **D:\\SymStore\\Symbols** folder and select **Properties**.

1. Select the **Sharing** tab.

1. Select **Advanced Sharing**.

1. In **Advanced Sharing**, select the **Share this folder** checkbox, and then select **Permissions**.

1. In **Share Permissions**, select **Everyone**, and then select **Remove**.

1. Select **Add** and enter the users or groups you want to access the file share.

1. For each user or group you add, select **Allow** to assign Full Control, Change, or Read permissions.

1. Select **Apply**, and then select **OK**.

1. Select **OK**, and then select **Close**.

### Computer Management

To assign file share permissions by using Computer Management:

1. Select and hold (or right-click) **Start** and select **Computer Management**.

1. In the console tree, select **System Tools** > **Shared Folders** > **Shares**.

1. Select and hold (or right-click) and select **New** > **Share**.

1. In **Create A Shared Folder Wizard**, select **Next**.

1. For **Folder path**, enter **D:\\SymStore\\Symbols**, and then select **Next**.

1. Select **Next**.

1. In **Shared Folder Permissions**, select **Customize permissions**, and then select **Custom**.

1. In **Share Permissions**, select **Everyone**, and then select **Remove**.

1. Select **Add** and enter the users or groups you want to access the file share.

1. For each user or group you add, select **Allow** to assign Full Control, Change, or Read permissions.

1. Select **Apply**, and then select **OK**.

1. Select **Finish** twice.

## Test the SMB file share

Configure a debugger to use this symbol path:

```text
srv*C:\Symbols*\\MachineName\Symbols
```

To view the location of the PDBs that are referenced in the debugger, use the `lm` (list modules) command. The paths to the PDBs should all begin with `C:\Symbols`.

To see logs of symbol and image downloads from the \\\\MachineName\\Symbols file server to C:\\Symbols, run `!sym noisy` and `.reload /f` .

## Set the file share symbol path

To configure your debugger’s symbol path (`.sympath`) to use a file share, you have multiple options. The syntax of the symbol path determines whether the symbol file is cached locally and where it's cached.

Direct file share use (no local caching):

```text
srv*\\MachineName\Symbols
```

Local caching of the file share’s files to a specific local folder (for example, to C:\\Symbols):

```text
srv*C:\Symbols*\\MachineName\Symbols
```

Local caching of the file share’s files to the %DBGHELP\_HOMEDIR%\\Sym folder:

```text
srv**\\MachineName\Symbols
```

The second "\*" in this example represents the default local server cache. For more information about setting the symbol path and use of the local cache, see [Symbol path for Windows debuggers](symbol-path.md).

If the `DBGHELP\_HOMEDIR` variable isn't set, `DBGHELP\_HOMEDIR` defaults to the debugger executable folder (for example, to C:\\Program Files\\Windows Kits\\10.0\\Debuggers\\x86) and caching occurs in C:\\Program Files\\Windows Kits\\10.0\\Debuggers\\x86\\Sym.

## See also

[Symbol store folder tree](symbol-store-folder-tree.md)
