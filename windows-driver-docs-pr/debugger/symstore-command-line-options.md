---
title: SymStore Command-Line Options
description: The following syntax forms are supported for SymStore transactions. The first parameter must always be add or del. The order of the other parameters is immaterial.
ms.assetid: 44009878-8f8a-4301-b075-eb0164b4f3a3
keywords: ["SymStore Command-Line Options Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- SymStore Command-Line Options
api_type:
- NA
ms.localizationpriority: medium
---

# SymStore Command-Line Options


The following syntax forms are supported for SymStore transactions. The first parameter must always be **add** or **del**. The order of the other parameters is immaterial.

```dbgcmd
symstore add [/r] [/p [/l] [-:MSG Message] [-:REL] [-:NOREFS]] /f File /s Store /t Product [/v Version] [/o] [/c Comment] [/d LogFile] [/compress]

symstore add [/r] [/p [/l] [-:REL] [-:NOREFS]] /g Share /f File /x IndexFile [/a] [/o] [/d LogFile] 

symstore add /y IndexFile /g Share /s Store [/p [-:MSG Message] [-:REL] [-:NOREFS]] /t Product [/v Version] [/o] [/c Comment] [/d LogFile] [/compress]

symstore query [/r] /f File /s Store [/o] [/d LogFile]

symstore del /i ID /s Store [/o] [/d LogFile] 

symstore /? 
```

## <span id="ddk_symstore_command_line_options_dbg"></span><span id="DDK_SYMSTORE_COMMAND_LINE_OPTIONS_DBG"></span>Parameters


<span id="________f_______File______"></span><span id="________f_______file______"></span><span id="________F_______FILE______"></span> **/f** *File*   
Specifies the network path of files or directories to add.

<span id="________g_______Share______"></span><span id="________g_______share______"></span><span id="________G_______SHARE______"></span> **/g** *Share*   
Specifies the server and share where the symbol files were originally stored. When used with **/f**, *Share* should be identical to the beginning of the *File* specifier. When used with **/y**, *Share* should be the location of the original symbol files (not the index file). This allows you to later change this portion of the file path in case you move the symbol files to a different server and share.

<span id="________s_______Store______"></span><span id="________s_______store______"></span><span id="________S_______STORE______"></span> **/s** *Store*   
Specifies the root directory for the symbol store.

<span id="________m_______Prefix______"></span><span id="________m_______prefix______"></span><span id="________M_______PREFIX______"></span> **/m** *Prefix*   
Causes SymStore to prefer using symbols from paths beginning with *Prefix* when storing files or updating pointers. This option cannot be used with the **/x** option.

<span id="________h___PUB___PRI__"></span><span id="________h___pub___pri__"></span><span id="________H___PUB___PRI__"></span> **/h** { **PUB | PRI** }  
Causes SymStore to prefer using public symbols (if PUB is specified), or private symbols (if PRI is specified) when storing or updating symbols. This option has no effect on binary files.

<span id="________i_______ID______"></span><span id="________i_______id______"></span><span id="________I_______ID______"></span> **/i** *ID*   
Specifies the transaction ID string.

<span id="________p______"></span><span id="________P______"></span> **/p**   
Causes SymStore to store a pointer to the file, rather than the file itself.

<span id="________l______"></span><span id="________L______"></span> **/l**   
Allows the file specified by *File* to be in a local directory rather than a network path. (This option can only be used when both **/f** and **/p** are used.)

<span id="_______-_MSG________Message______"></span><span id="_______-_msg________message______"></span><span id="_______-_MSG________MESSAGE______"></span> **-:MSG** *Message*   
Adds the specified *Message* to each file. (This option can only be used when **/p** is used.)

<span id="_______-_REL______"></span><span id="_______-_rel______"></span> **-:REL**   
Allows the paths in the file pointers to be relative. This option implies the /**l** option. (This option can only be used when **/p** is used.)

<span id="_______-_NOREFS______"></span><span id="_______-_norefs______"></span> **-:NOREFS**   
Omits the creation of reference pointer files for the files and pointers being stored. This option is only valid during the initial creation of a symbol store if the store being changed was created with this option.

<span id="________r______"></span><span id="________R______"></span> **/r**   
Causes SymStore to add files or directories recursively.

<span id="________t_______Product______"></span><span id="________t_______product______"></span><span id="________T_______PRODUCT______"></span> **/t** *Product*   
Specifies the name of the product.

<span id="________v_______Version______"></span><span id="________v_______version______"></span><span id="________V_______VERSION______"></span> **/v** *Version*   
Specifies the version of the product.

<span id="________c_______Comment______"></span><span id="________c_______comment______"></span><span id="________C_______COMMENT______"></span> **/c** *Comment*   
Specifies a comment for the transaction.

<span id="________d_______LogFile______"></span><span id="________d_______logfile______"></span><span id="________D_______LOGFILE______"></span> **/d** *LogFile*   
Specifies a log file to be used for command output. If this is not included, transaction information and other output is sent to **stdout**.

<span id="________o______"></span><span id="________O______"></span> **/o**   
Causes SymStore to display verbose output.

<span id="________x_______IndexFile______"></span><span id="________x_______indexfile______"></span><span id="________X_______INDEXFILE______"></span> **/x** *IndexFile*   
Causes SymStore not to store the actual symbol files. Instead, SymStore records information in the *IndexFile* that will enable SymStore to access the symbol files at a later time.

<span id="________a______"></span><span id="________A______"></span> **/a**   
Causes SymStore to append new indexing information to an existing index file. (This option is only used with the **/x** option.)

<span id="________y_______IndexFile______"></span><span id="________y_______indexfile______"></span><span id="________Y_______INDEXFILE______"></span> **/y** *IndexFile*   
Causes SymStore to read the data from a file created with **/x**.

<span id="________yi_______IndexFile______"></span><span id="________yi_______indexfile______"></span><span id="________YI_______INDEXFILE______"></span> **/yi** *IndexFile*   
Appends a comment with the transaction ID to the end of an index file created with the /**x** option.

<span id="________z___PUB___PRI__"></span><span id="________z___pub___pri__"></span><span id="________Z___PUB___PRI__"></span> **/z** { **PUB | PRI** }  
Causes SymStore to index only the type of symbols specified. If **PUB** is specified, then only the symbols that have had the full source information stripped will be indexed. If **PRI** is specified, then only the symbols that contain the full source information will be indexed. SymStore will always index binary symbols.

<span id="________compress______"></span><span id="________COMPRESS______"></span> **/compress**   
Causes SymStore to create a compressed version of each file copied to the symbol store instead of using an uncompressed copy of the file. This option is only valid when storing files and not pointers, and consequently cannot be used when the **/p** option is used.

<span id="_______________"></span> **/?**   
Displays help text for the SymStore command.

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information about SymStore, see [Using Symbol Servers and Symbol Stores](symbol-stores-and-symbol-servers.md).









