---
title: SymStore Transactions
description: SymStore Transactions
ms.assetid: f0bb2f3f-0f6b-4ed6-809e-f55b1c537d7f
keywords: ["SymStore, transactions"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# SymStore Transactions


## <span id="ddk_symbol_files_overview_dbg"></span><span id="DDK_SYMBOL_FILES_OVERVIEW_DBG"></span>


Every call to SymStore is recorded as a transaction. There are two types of transactions: add and delete.

When the symbol store is created, a directory, called "000admin", is created under the root of the server. The 000admin directory contains one file for each transaction, as well as the log files server.txt and history.txt. The server.txt file contains a list of all transactions that are currently on the server. The history.txt file contains a chronological history of all transactions.

Each time SymStore stores or removes symbol files, a new transaction number is created. Then, a file, whose name is this transaction number, is created in 000admin. This file contains a list of all the files or pointers that have been added to the symbol store during this transaction. If a transaction is deleted, SymStore will read through its transaction file to determine which files and pointers it should delete.

The **add** and **del** options specify whether an add or delete transaction is to be performed. Including the **/p** option with an add operation specifies that a pointer is to be added; omitting the **/p** option specifies that the actual symbol file is to be added.

It is also possible to create the symbol store in two separate stages. In the first stage, you use SymStore with the **/x** option to create an index file. In the second stage, you use SymStore with the **/y** option to create the actual store of files or pointers from the information in the index file.

This can be a useful technique for a variety of reasons. For instance, this allows the symbol store to be easily recreated if the store is somehow lost, as long as the index file still exists. Or perhaps the computer containing the symbol files has a slow network connection to the computer on which the symbol store will be created. In this case, you can create the index file on the same machine as the symbol files, transfer the index file to the second machine, and then create the store on the second machine.

For a full listing of all SymStore parameters, see [**SymStore Command-Line Options**](symstore-command-line-options.md).

**Note**   SymStore does not support simultaneous transactions from multiple users. It is recommended that one user be designated "administrator" of the symbol store and be responsible for all **add** and **del** transactions.

 

### <span id="transaction_examples"></span><span id="TRANSACTION_EXAMPLES"></span>Transaction Examples

Here are two examples of SymStore adding symbol pointers for build 2195 of Windows 2000 to \\\\MyDir\\symsrv:

```console
symstore add /r /p /f \\BuildServer\BuildShare\2195free\symbols\*.* /s \\MyDir\symsrv /t "Windows 2000" /v "Build 2195 x86 free" /c "Sample add"
symstore add /r /p /f \\BuildServer\BuildShare\2195free\symbols\*.* /s \\MyDir\symsrv /t "Windows 2000" /v "Build 2195 x86 checked" /c "Sample add"
```

In the following example, SymStore adds the actual symbol files for an application project in \\\\largeapp\\appserver\\bins to \\\\MyDir\\symsrv:

```console
symstore add /r /f \\largeapp\appserver\bins\*.* /s \\MyDir\symsrv /t "Large Application" /v "Build 432" /c "Sample add"
```

Here is an example of how an index file is used. First, SymStore creates an index file based on the collection of symbol files in \\\\largeapp\\appserver\\bins\\. In this case, the index file is placed on a third computer, \\\\hubserver\\hubshare. You use the **/g** option to specify that the file prefix "\\\\largeapp\\appserver" might change in the future:

```console
symstore add /r /p /g \\largeapp\appserver /f \\largeapp\appserver\bins\*.* /x \\hubserver\hubshare\myindex.txt
```

Now suppose you move all the symbol files off of the machine \\\\largeapp\\appserver and put them on \\\\myarchive\\appserver. You can then create the symbol store itself from the index file \\\\hubserver\\hubshare\\myindex.txt as follows:

```console
symstore add /y \\hubserver\hubshare\myindex.txt /g \\myarchive\appserver /s \\MyDir\symsrv /p /t "Large Application" /v "Build 432" /c "Sample Add from Index"
```

Finally, here is an example of SymStore deleting a file added by a previous transaction. See "The server.txt and history.txt Files" section below for an explanation of how to determine the transaction ID (in this case, 0000000096).

```console
symstore del /i 0000000096 /s \\MyDir\symsrv
```

### <span id="the_server_txt_and_history_txt_files"></span><span id="THE_SERVER_TXT_AND_HISTORY_TXT_FILES"></span>The server.txt and history.txt Files

When a transaction is added, several items of information are added to server.txt and history.txt for future lookup capability. The following is an example of a line in server.txt and history.txt for an add transaction:

```text
0000000096,add,ptr,10/09/99,00:08:32,Windows Vista SP 1,x86 fre 1.156c-RTM-2,Added from \\mybuilds\symbols,
```

This is a comma-separated line. The fields are explained as follows:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Field</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>0000000096</p></td>
<td align="left"><p>Transaction ID number, as created by SymStore.</p></td>
</tr>
<tr class="even">
<td align="left"><p>add</p></td>
<td align="left"><p>Type of transaction. This field can be either <strong>add</strong> or <strong>del</strong>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>ptr</p></td>
<td align="left"><p>Whether files or pointers were added. This field can be either <strong>file</strong> or <strong>ptr</strong>.</p></td>
</tr>
<tr class="even">
<td align="left"><p>10/09/99</p></td>
<td align="left"><p>Date when transaction occurred.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>00:08:32</p></td>
<td align="left"><p>Time when transaction started.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Windows Vista SP 1</p></td>
<td align="left"><p>Product.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>x86 fre</p></td>
<td align="left"><p>Version (optional).</p></td>
</tr>
<tr class="even">
<td align="left"><p>Added from</p></td>
<td align="left"><p>Comment (optional)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Unused</p></td>
<td align="left"><p>(Reserved for later use.)</p></td>
</tr>
</tbody>
</table>

 

Here are some sample lines from the transaction file 0000000096. Each line records the directory and the location of the file or pointer that was added to the directory.

```text
canon800.dbg\35d9fd51b000,\\mybuilds\symbols\sp4\dll\canon800.dbg
canonlbp.dbg\35d9fd521c000,\\mybuilds\symbols\sp4\dll\canonlbp.dbg
certadm.dbg\352bf2f48000,\\mybuilds\symbols\sp4\dll\certadm.dbg
certcli.dbg\352bf2f1b000,\\mybuilds\symbols\sp4\dll\certcli.dbg
certcrpt.dbg\352bf04911000,\\mybuilds\symbols\sp4\dll\certcrpt.dbg
certenc.dbg\352bf2f7f000,\\mybuilds\symbols\sp4\dll\certenc.dbg
```

If you use a **del** transaction to undo the original **add** transactions, these lines will be removed from server.txt, and the following line will be added to history.txt:

```text
0000000105,del,0000000096
```

The fields for the delete transaction are described as follows.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Field</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>0000000105</p></td>
<td align="left"><p>Transaction ID number, as created by SymStore.</p></td>
</tr>
<tr class="even">
<td align="left"><p>del</p></td>
<td align="left"><p>Type of transaction. This field can be either <strong>add</strong> or <strong>del</strong>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0000000096</p></td>
<td align="left"><p>Transaction that was deleted.</p></td>
</tr>
</tbody>
</table>

 

 

 





