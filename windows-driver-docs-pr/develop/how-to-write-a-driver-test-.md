---
ms.assetid: 79AB7242-72D6-4198-9AF0-482CBFB756C7
title: How to write a driver test using a Driver Test template
description: Use the Windows Driver Kit (WDK) for Windows 8 to create your own driver tests or to customize some of the tests that are provided.
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# How to write a driver test using a Driver Test template

You can use the Windows Driver Kit (WDK) for Windows 8 to create your own driver tests or to customize some of the tests that are provided. You can deploy the tests that you create to remote test computers using the driver testing framework that the WDK provides for Microsoft Visual Studio Ultimate 2012.

The WDK provides templates that create starter code for a Windows Driver test project in C++, C\#, and Script (JScript). You can select the test cases that you want to include, or you can start with a blank project. You can customize the code to add new test cases for your driver. You can deploy your tests from Visual Studio using the driver test framework.

## <span id="To_customize_a_driver_test_using_the_Driver_Test_template_for_C__"></span><span id="to_customize_a_driver_test_using_the_driver_test_template_for_c__"></span><span id="TO_CUSTOMIZE_A_DRIVER_TEST_USING_THE_DRIVER_TEST_TEMPLATE_FOR_C__"></span>To customize a driver test using the Driver Test template for C++


1.  From the **File** menu, click **New &gt; Project**.
2.  From the list of installed templates in the **New Project** dialog box, select **Visual C++ &gt; Windows Driver &gt; Tests**.
3.  Select **Windows Driver Test in C++**.
4.  Provide a name for your driver test project and a location (or use the default).
5.  From the **Windows Driver Test** dialog box, select the test cases that you want to include or choose an empty (blank) driver test. For more information about the test cases, see [Windows Driver test cases](#windows_driver_test_cases).
6.  Add the required test metadata. For more information, see [How to add test metadata](to-add-test-metadata.md).
7.  Build your driver test.

## <span id="To_customize_a_driver_test_using_the_Driver_Test_template_for_C_"></span><span id="to_customize_a_driver_test_using_the_driver_test_template_for_c_"></span><span id="TO_CUSTOMIZE_A_DRIVER_TEST_USING_THE_DRIVER_TEST_TEMPLATE_FOR_C_"></span>To customize a driver test using the Driver Test template for C\#


1.  From the **File** menu, click **New &gt; Project**.
2.  From the list of installed templates in the **New Project** dialog box, select **Visual C\# &gt; Windows Driver** .
3.  Select **Windows Driver Test in C\#**.
4.  Provide a name for your driver test project and a location (or use the default).
5.  From the **Windows Driver Test** dialog box, select the test cases that you want to include or choose an empty (blank) driver test. For information about the test cases, see [Windows Driver test cases](#windows_driver_test_cases).
6.  Add the required test metadata. For more information, see [How to add test metadata](to-add-test-metadata.md).
7.  Build your driver test.

## <span id="To_customize_a_driver_test_using_the_Driver_Test_template_for_Script"></span><span id="to_customize_a_driver_test_using_the_driver_test_template_for_script"></span><span id="TO_CUSTOMIZE_A_DRIVER_TEST_USING_THE_DRIVER_TEST_TEMPLATE_FOR_SCRIPT"></span>To customize a driver test using the Driver Test template for Script


1.  From the **File** menu, click **New &gt; Project**.
2.  From the list of installed templates in the **New Project** dialog box, select **Script &gt; Windows Driver** .
3.  Select **Windows Driver Test Script**.
4.  Provide a name for your driver test project and a location (or use the default).
5.  From the **Windows Driver Test** dialog box, select the test cases that you want to include or choose an empty (blank) driver test. For information about the test cases, see [Windows Driver test cases](#windows_driver_test_cases).
6.  Add the required test metadata. For more information, see [How to add test metadata](to-add-test-metadata.md).
7.  Build your driver test.

## <span id="Making_the_driver_tests_you_create_available_for_deployment_on_test_computers"></span><span id="making_the_driver_tests_you_create_available_for_deployment_on_test_computers"></span><span id="MAKING_THE_DRIVER_TESTS_YOU_CREATE_AVAILABLE_FOR_DEPLOYMENT_ON_TEST_COMPUTERS"></span>Making the driver tests you create available for deployment on test computers


When you build your driver test, the new test will be available for deployment to a test computer. By default, the tests that you create will appear in the test category **My Test Category**. The names of the tests are based upon the test cases that you choose, and they will have names such as **My Plug and Play Surprise Remove Test**. During each build of the test, the test will be overwritten. The latest build of the test will be available to deploy and run on the test computer.

## <span id="windows_driver_test_cases"></span><span id="WINDOWS_DRIVER_TEST_CASES"></span>Windows Driver test cases


The WDK provides starter code for a Windows Driver test project in C++, C\#, and Script. You can select test cases that you want to include, or you can start with a blank project. Not all test cases are available in every language.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Plug and Play Test Cases</th>
<th align="left">Test cases that force a driver to handle most of the Plug and Play (PnP)-related IRPs</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left">Disable/Enable</td>
<td align="left">Provides code for test cases that disable and enable a PnP device.</td>
</tr>
<tr class="even">
<td align="left">Remove</td>
<td align="left">Provides code for test cases that remove a PnP device.</td>
</tr>
<tr class="odd">
<td align="left">Surprise Remove</td>
<td align="left">Provides code for test cases that perform a surprise remove of a PnP device.</td>
</tr>
<tr class="even">
<td align="left">Power Management Test Cases</td>
<td align="left">Provides test cases that force a driver to handle system sleep states.</td>
</tr>
<tr class="odd">
<td align="left">System Sleep States</td>
<td align="left">Provides code for test cases that perform device I/O while the system cycles through sleep and power state.</td>
</tr>
<tr class="even">
<td align="left">Stress and Functionality Test Cases</td>
<td align="left">Provides test cases that perform I/O stress and function testing of IOCTL and WMI interfaces.</td>
</tr>
<tr class="odd">
<td align="left">I/O Stress</td>
<td align="left">Provides test cases that perform device I/O stress.</td>
</tr>
<tr class="even">
<td align="left">Functional IOCTL Interface</td>
<td align="left">Provides a template for creating functional test cases for the IOCTL interface. (only available for C++ ).</td>
</tr>
<tr class="odd">
<td align="left">Functional WMI Interface</td>
<td align="left">Provides a template for creating functional test cases for the Windows Management Interface (WMI). (only available in Script)</td>
</tr>
<tr class="even">
<td align="left">Empty Test Case</td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left"></td>
<td align="left">Provides a blank template for creating a Windows Driver test project.</td>
</tr>
</tbody>
</table>

 

## <span id="related_topics"></span>Related topics


* [Test Authoring and Execution Framework](https://msdn.microsoft.com/Library/Windows/Hardware/Hh439725)
* [Windows Driver Testing Framework](https://msdn.microsoft.com/Library/Windows/Hardware/Ff539547)
* [How to add test metadata](to-add-test-metadata.md)
 

 






