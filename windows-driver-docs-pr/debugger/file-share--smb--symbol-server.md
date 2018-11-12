---
title: File Share (SMB) Symbol Server
description: Running a SMB Symbol Server is simply a matter of creating a file share and granting users access to that file share.
ms.assetid: C5CF9665-9289-48EB-AA12-8881F812488A
ms.author: domars
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# File Share (SMB) Symbol Server


Running a SMB Symbol Server is simply a matter of creating a file share and granting users access to that file share.

## <span id="Creating_a_SMB_File_Share_Symbol_Store_"></span><span id="creating_a_smb_file_share_symbol_store_"></span><span id="CREATING_A_SMB_FILE_SHARE_SYMBOL_STORE_"></span>Creating a SMB File Share Symbol Store


Use Windows Explorer or Computer Management to create the File Share and assign security. These steps assume that the symbols will be located in *D:\\SymStore\\Symbols*. Complete these steps using Windows Explorer:

1. Open **Windows Explorer**.

2. Right-click *D:\\SymStore\\Symbols* and choose **Properties**.

3. Click on the **Sharing** tab.

4. Click on **Advanced Sharing**… .

5. Check *Share this folder*.

6. Click on **Permissions**.

7. Remove the *Everyone* group.

8. Using **Add…**, add the Users/Security Groups requiring access.

9. For each User/Security Group added, grant Read or Read/Change access.

10. Click on **OK** (Permissions dialog).

11. Click on **OK** (Advanced Sharing dialog).

12. Press **Close** (Properties dialog).

Complete these steps using Computer Management:

1. Type *Computer* in Window Start (resolves as This PC in Windows 8).

2. Right-click and select *Manage*.

3. Navigate to *System Tools | Shared Folders | Shares*.

4. Right-click and select **New | Share…** .

5. Press **Next** (Create a Shared Folder Wizard dialog).

6. Enter **D:\\SymStore\\Symbols** as the Folder Path.

7. Press **Next** twice.

8. Select **Customize permissions**.

9. Press **Custom…** .

10. Remove *Everyone*.

11. Using **Add…**, add the Users/Security Groups requiring access.

12. For each User/Security Group added, grant Read or Read/Change access.

13. Press **OK** (Customize Permissions dialog).

14. Press **Finish** twice to complete the process.

## <span id="Test_The_SMB_File_Share"></span><span id="test_the_smb_file_share"></span><span id="TEST_THE_SMB_FILE_SHARE"></span>Test The SMB File Share


Configure a debugger to use this symbol path:

```text
srv*C:\Symbols*\\MachineName\Symbols
```

To view the location of the PDBs being referenced in the debugger, use the lm (list modules) command. The path to the PDBs should all begin with C:\\Symbols. By running “!sym noisy”, and “.reload /f”, you will see extensive symbol logging of the download of the symbols and images from the \\\\MachineName\\Symbols file server to C:\\Symbols.

## <span id="File_Share_Symbol_Path"></span><span id="file_share_symbol_path"></span><span id="FILE_SHARE_SYMBOL_PATH"></span>File Share Symbol Path


There are multiples ways to configure your debugger’s symbol path (.sympath) to use a File Share. The syntax of the symbol path determines if the symbol file will be cached locally or not, and where it is cached.

Direct File Share use (no local caching):

```text
srv*\\MachineName\Symbols
```

Local Caching of the File Share’s files to a particular local folder (e.g. c:\\Symbols):

```text
srv*c:\Symbols*\\MachineName\Symbols
```

Local Caching of the File Share’s files to the %DBGHELP\_HOMEDIR%\\Sym folder:

```text
srv**\\MachineName\Symbols
```

The second “\*” in the example shown above, represents the default local server cache.

If the DBGHELP\_HOMEDIR variable is not set, DBGHELP\_HOMEDIR defaults to the debugger executable folder (for example C:\\Program Files\\Windows Kits\\10.0\\Debuggers\\x86) and causes caching to occur in C:\\Program Files\\Windows Kits\\10.0\\Debuggers\\x86\\Sym.

## <span id="related_topics"></span>Related topics


[Symbol Store Folder Tree](symbol-store-folder-tree.md)

 

 






