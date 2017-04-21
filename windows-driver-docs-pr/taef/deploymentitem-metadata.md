---
title: DeploymentItem Metadata
description: DeploymentItem Metadata
ms.assetid: 7F18CD71-F000-4231-9093-82980EB7584D
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# DeploymentItem Metadata


**DeploymentItem** metadata identifies file and folder dependencies for the files and folders that are used by the tests during the tests' execution so that Taef could be able to identify these and copy them appropriately (for example, in a [cross machine execution scenario](cross-machine-execution.md), Taef will deploy the files identified by **DeploymentItem** property to the specified test machine).

Taef DeploymentItem implementation is very similar to the [similar functionality of VSTS](http://msdn.microsoft.com/library/microsoft.visualstudio.testtools.unittesting.deploymentitemattribute(VS.80).aspx).

DeploymentItem metadata can be applied on either assembly, class, or test level. The items specified by DeploymentItem metadata will be deployed by the time correspondent (assembly, test class or test) setup runs. If DeploymentItem metadata specifies a dependency (for example, a file) and that dependency already exists at the destination, TAEF does a CRC comparison and only copies the file if it has changed. If DeploymentItem metadata specifies a dependency and the dependency cannot be found, an error is logged that will fail the test (or all test class or assembly tests, accordingly). TAEF will only deploy files once per assembly, class, or test - that is, the deployment does not happen at every assembly, class, or test expansion if these are data driven.

## <span id="Syntax"></span><span id="syntax"></span><span id="SYNTAX"></span>Syntax


<span id="General_Usage_"></span><span id="general_usage_"></span><span id="GENERAL_USAGE_"></span>General Usage   

<span id="_DeploymentItem__FileOrFolderToDeploy____DestinationFolder___"></span><span id="_deploymentitem__fileorfoldertodeploy____destinationfolder___"></span><span id="_DEPLOYMENTITEM__FILEORFOLDERTODEPLOY____DESTINATIONFOLDER___"></span>\[DeploymentItem("FileOrFolderToDeploy", "DestinationFolder")\]  
where

<span id="FileOrFolderToDeploy"></span><span id="fileorfoldertodeploy"></span><span id="FILEORFOLDERTODEPLOY"></span>FileOrFolderToDeploy  
is a file or a folder path relative to the directory where test dll is. If **FileOrFolderToDeploy** is a folder, all its contents is copied; however, the folder itself does not get created. If there is a hierarchy of folders under **FileOrFolderToDeploy**, Taef will copy all these directories recursively, maintaining their directory hierarchy.

<span id="DestinationFolder"></span><span id="destinationfolder"></span><span id="DESTINATIONFOLDER"></span>DestinationFolder  
is a folder path relative to the directory where the test dll is and where the deployment items are copied. **DestinationFolder** path could be specified using .. notation (for example, ..\\MyFiles).

If you just want to deploy to the folder where your test dll is, **DestinationFolder** could be omitted:

```
[DeploymentItem("FileOrFolderToDeploy")]
```

Multiple pieces of the property are supported. For example:

```
[TestClass]
[DeploymentItem("file1.xml")]
[DeploymentItem("file2.xml")]
[DeploymentItem("file3.xml")]
public class UnitTest1
{
    ...
}
                
```

## <span id="Examples"></span><span id="examples"></span><span id="EXAMPLES"></span>Examples


<span id="_deploymentitem__file1.xml___"></span><span id="_DEPLOYMENTITEM__FILE1.XML___"></span>\[DeploymentItem("file1.xml")\]  
Tags file1.xml that is located next to the test dll as a dependency. This metadata could be interpreted as that the system deploys an item named file1.xml located in the folder next to the test dll to the test dll directory. This configuration is only useful for cross machine scenario.

<span id="_deploymentitem__file2.xml____datafiles___"></span><span id="_DEPLOYMENTITEM__FILE2.XML____DATAFILES___"></span>\[DeploymentItem("file2.xml", "DataFiles")\]  
Deploys an item named file2.xml located next to the test dll to the created DataFiles subdirectory in the test dll directory.

<span id="_DeploymentItem__C___MyDataFiles__MyDataFiles2_____"></span><span id="_deploymentitem__c___mydatafiles__mydatafiles2_____"></span><span id="_DEPLOYMENTITEM__C___MYDATAFILES__MYDATAFILES2_____"></span>\[DeploymentItem("C:\\\\MyDataFiles\\\\MyDataFiles2\\\\")\]  
Deploys all items and directories found within the C:\\\\MyDataFiles\\\\MyDataFiles2\\\\ directory. This configuration does not create the MyDataFiles\\MyDataFiles2 directory underneath the deployment directory. All files and directories within MyDataFiles will be deployed to test dll directory. To copy the entire MyDataFiles\\MyDataFiles2 directory structure, you must specify MyDataFiles\\MyDataFiles2 as an output directory.

<span id="_deploymentitem___mydir__myfile.txt___"></span><span id="_DEPLOYMENTITEM___MYDIR__MYFILE.TXT___"></span>\[DeploymentItem("%myDir%\\myFile.txt")\]  
Deploys the file myFile.txt if that file exists in the directory to which %myDir% resolves. If TAEF is unable to resolve the environment variable, it throws an error.

## <span id="Managed_Tests"></span><span id="managed_tests"></span><span id="MANAGED_TESTS"></span>Managed Tests


The **DeploymentItem** (aka DeploymentItemAttribute) attribute can be applied to a test method (decorated by \[TestMethod\] attribute), test class (decorated by \[TestClass\] attribute) or test assembly. However, since VSTS does not support this property on assembly level, to apply this property on assembly level, you have to apply it to assembly setup (decorated by AssemblyInitialize attribute):

```
[AssemblyInitialize]
[DeploymentItem("file1.xml")]
[DeploymentItem("file2.xml")]
[DeploymentItem("file3.xml")]
public  static AssemblySetup(TestContext testContext)
{
    ...
}
                
```

## <span id="Native_Tests"></span><span id="native_tests"></span><span id="NATIVE_TESTS"></span>Native Tests


For native tests, the property format is similar to the managed code format. However, since native properties only have a single value, the item path and optional destination are specified in the property value, separated with a **'&gt;'** character:

```
BEGIN_TEST_CLASS(TestClassExample)
    TEST_CLASS_PROPERTY(L"DeploymentItem", L"C:\\Dependencies\\>Dependencies")
END_TEST_CLASS()
                
```

## <span id="Script_Tests"></span><span id="script_tests"></span><span id="SCRIPT_TESTS"></span>Script Tests


For script tests, the property format is the same as for native tests:

```
<method name="TestOne">
    <TestMethodProperty name="DeploymentItem" value="C:\\Dependencies\\>Dependencies"/>
</method>
                
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[taef\taef]:%20DeploymentItem%20Metadata%20%20RELEASE:%20%289/12/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




