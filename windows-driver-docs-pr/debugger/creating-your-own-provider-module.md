---
title: Creating Your Own Provider Module
description: Creating Your Own Provider Module
ms.assetid: 4282d375-bcf0-478f-bb2f-a43dc50b09e3
keywords: ["version control systems, provider modules"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Creating Your Own Provider Module


In general, to create your own provider module, you must implement the following set of interfaces.

<span id="_module__SimpleUsage__"></span><span id="_module__simpleusage__"></span><span id="_MODULE__SIMPLEUSAGE__"></span>**$module::SimpleUsage()**  

<span id="Purpose"></span><span id="purpose"></span><span id="PURPOSE"></span>**Purpose**  
Displays simple module usage information to STDOUT.

<span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>**Parameters**  
None

<span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>**Return Value**  
None

<span id="_module__VerboseUsage__"></span><span id="_module__verboseusage__"></span><span id="_MODULE__VERBOSEUSAGE__"></span>**$module::VerboseUsage()**  

<span id="Purpose"></span><span id="purpose"></span><span id="PURPOSE"></span>**Purpose**  
Displays in-depth module usage information to STDOUT.

<span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>**Parameters**  
None

<span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>**Return Value**  
None

<span id="_objref____module__new__CommandArguments_"></span><span id="_objref____module__new__commandarguments_"></span><span id="_OBJREF____MODULE__NEW__COMMANDARGUMENTS_"></span>**$objref = $module::new(**<em>@CommandArguments</em>**)**  

<span id="Purpose"></span><span id="purpose"></span><span id="PURPOSE"></span>**Purpose**  
Initializes an instance of the provider module.

<span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>**Parameters**  

<span id="_CommandArguments"></span><span id="_commandarguments"></span><span id="_COMMANDARGUMENTS"></span><em>@CommandArguments</em>  
All @ARGV arguments that are not recognized by ssindex.cmd as being general arguments.

<span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>**Return Value**  
A reference that can be used in later operations.

<span id="_objref-_GatherFileInformation__SourcePath__ServerHashReference_"></span><span id="_objref-_gatherfileinformation__sourcepath__serverhashreference_"></span><span id="_OBJREF-_GATHERFILEINFORMATION__SOURCEPATH__SERVERHASHREFERENCE_"></span>**$objref-&gt;GatherFileInformation(**<em>$SourcePath</em>**,**<em>$ServerHashReference</em>**)**  

<span id="Purpose"></span><span id="purpose"></span><span id="PURPOSE"></span>**Purpose**  
Enables the module to gather the required source-indexing information for the directory specified by the *$SourcePath* parameter. The module should not assume that this entry is called only once for each object instancebecause SSIndex may call it multiple times for different paths.

<span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>**Parameters**  

<span id="_SourcePath"></span><span id="_sourcepath"></span><span id="_SOURCEPATH"></span>*$SourcePath*  
The local directory containing the source to be indexed.

<span id="_ServerHashReference"></span><span id="_serverhashreference"></span><span id="_SERVERHASHREFERENCE"></span>*$ServerHashReference*  
A reference to a hash containing all of the entries from the specified Srcsrv.ini file.

<span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>**Return Value**  
None

<span id="__VariableHashReference__FileEntry_____objref-_GetFileInfo__LocalFile_"></span><span id="__variablehashreference__fileentry_____objref-_getfileinfo__localfile_"></span><span id="__VARIABLEHASHREFERENCE__FILEENTRY_____OBJREF-_GETFILEINFO__LOCALFILE_"></span>**(**<em>$VariableHashReference</em>**,**<em>$FileEntry</em>**) = $objref**-&gt;**GetFileInfo(**<em>$LocalFile</em>**)**  

<span id="Purpose"></span><span id="purpose"></span><span id="PURPOSE"></span>**Purpose**  
Provides the necessary information to extract a single, specific file from the source control system.

<span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>**Parameters**  

<span id="_LocalFile"></span><span id="_localfile"></span><span id="_LOCALFILE"></span>*$LocalFile*  
A fully qualified file name.

<span id="Return_Values"></span><span id="return_values"></span><span id="RETURN_VALUES"></span>**Return Values**  

<span id="_VariableHashReference"></span><span id="_variablehashreference"></span><span id="_VARIABLEHASHREFERENCE"></span>*$VariableHashReference*  
A hash reference of the variables necessary to interpret the returned *$FileEntry*. Ssindex.cmd caches these variables for every source file used by a single debug file to reduce the amount of information written to the source index stream.

<span id="_FileEntry"></span><span id="_fileentry"></span><span id="_FILEENTRY"></span>*$FileEntry*  
The file entry to be written to the source index stream to allow SrcSrv to extract this file from source control. The exact format of this line is specific to the source control system.

<span id="_TextString___objref-_LongName__"></span><span id="_textstring___objref-_longname__"></span><span id="_TEXTSTRING___OBJREF-_LONGNAME__"></span><em>$TextString</em>**= $objref-&gt;LongName()**  

<span id="Purpose"></span><span id="purpose"></span><span id="PURPOSE"></span>**Purpose**  
Provides a descriptive string to identify the source control system to the end user.

<span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>**Parameters**  
None

<span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>**Return Value**  

<span id="_TextString"></span><span id="_textstring"></span><span id="_TEXTSTRING"></span>*$TextString*  
The descriptive name of the source control system.

<span id="_StreamVariableLines__objref-_SourceStreamVariables__"></span><span id="_streamvariablelines__objref-_sourcestreamvariables__"></span><span id="_STREAMVARIABLELINES__OBJREF-_SOURCESTREAMVARIABLES__"></span><strong>@StreamVariableLines=$objref-&gt;SourceStreamVariables()</strong>  

<span id="Purpose"></span><span id="purpose"></span><span id="PURPOSE"></span>**Purpose**  
Enables the source control system to add source-control-specific variables to the source stream for each debug file. The sample modules use this method for writing the required EXTRACT\_CMD and EXTRACT\_TARGET variables.

<span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>**Parameters**  
None

<span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>**Return Value**  

<span id="_StreamVariableLines"></span><span id="_streamvariablelines"></span><span id="_STREAMVARIABLELINES"></span><em>@StreamVariableLines</em>  
The list of entries for the source stream variables.

 

 





