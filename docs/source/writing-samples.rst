
.. _writing-samples:


Writing Samples
###############

All of the samples below were targeted towards software developers using the Intel®
oneAPI suite of complilers, libraries, and tools. 

`Intel® oneAPI Programming Guide Development Environment Setup <https://www.intel.com/content/www/us/en/docs/oneapi/programming-guide/2024-2/oneapi-development-environment-setup.html>`_


:download:`PDF Version, starting on page 15 <pdf/oneapi-programming-guide.pdf>`

..

   **Project**

     Introduce a new default installation directory for both Windows and Linux.

   **Context** 

     The Environment Setup page is one of the most important parts of the Programming
     Guide, and it frequently changes. When the default installation directory changed, users who
     accept default directories
     would need to customize configuration files, point scripts to the new location
     for libraries and compilers, and alter their PATH.
   
   **Achievements**

     - informed users of advantages of the new layout
     - increased usability for users by describing configuration options
     - engineering verified content was accurate
     - validation verified that procedures were accurate
     - updated 180 documents to mention this section and point users to this section for more information
  
  **Technical Details**

     Source files: reStructuredText
     Repository: internal GitHub repository
     Transformation: Sphinx to DITA (sphinx2dita)
     Web Platform: Adobe Experience Manager (AEM) 



`How to use CMake with Intel® oneAPI Toolkits <https://www.intel.com/content/www/us/en/developer/articles/technical/how-to-use-cmake-with-intel-oneapi-toolkits.html>`_ 

:download:`PDF Version <pdf/cmake-article.pdf>`

..

   **Project**

     Explain how users can configure CMake to automatically trigger configuration options.

   **Context**

     With the December 2023 release, configuration options changed so that users had options when
     configuring their systems. I worked with a developer to write this article, publish, and promote the article.

   **Achievements**

     - educated users on new configuration options using CMake
     - reduced duplicate text in multiple documents by pointing users to this article when dealing with CMake options

   **Technical Details**

     Source file: AEM article
     Repository: AEM article editor
     Web Platform: Adobe Experience Manager (AEM) 


`Get Started with the Intel® oneAPI Base Toolkit for Linux <https://www.intel.com/content/www/us/en/docs/oneapi-base-toolkit/get-started-guide-linux/2024-0/overview.html>`_


:download:`PDF Version <pdf/oneapi-base-toolkit_get-started-guide-linux.pdf>`

..

   **Project**

     Provide a quick path for users to be able to verify installation, configure their system, and run a sample.

   **Context**

     I originally created this for the first beta release of the Intel® oneAPI Base Toolkit. I worked with the
     Developer Experience team to run user studies to improve the get started experience both from a technical
     standpoint and from a documentation standpoint. The 2024.0 version was the last version I worked on, after
     two years of quarterly releases.

   **Achievements**

     - improved user success in user studies by more than 40 percent
     - directed users to troubleshooting steps when commands produced error messages
     - integrated installed samples with GitHub samples to enable users to experiment with different functions 

   **Technical Details**

     Source files: DITA XML
     Repository: SDL Trisoft Publication Manager
     Transformation: SDL publication to DITA XML
     Web Platform: Adobe Experience Manager (AEM) 



UI Writing Samples
******************

`Get Started with the Intel® oneAPI Base Toolkit for Windows <https://www.intel.com/content/www/us/en/docs/oneapi-base-toolkit/get-started-guide-windows/2024-0/run-a-sample-project-with-vscode.html>`_

:download:`PDF Version <pdf/oneapi-base-toolkit_get-started-guide-windows.pdf>`

..

   **Project**

     Provide a quick path for users to be able to verify installation, configure their system, and run a sample.

   **Context**

     I originally created this for the first beta release of the Intel® oneAPI Base Toolkit. I worked with the
     Developer Experience team to run user studies to improve the get started experience both from a technical
     standpoint and from a documentation standpoint. The 2024.0 version was the last version I worked on, after
     two years of quarterly releases.

   **Achievements**

     - improved user success for configuration in user studies by more than 40 percent
     - directed users to troubleshooting steps when the UI produced error messages
     - integrated installed samples with GitHub samples to enable users to experiment with different functions 


   **Technical Details**

     Source files: DITA XML
     Repository: SDL Trisoft Publication Manager
     Transformation: SDL publication to DITA XML
     Web Platform: Adobe Experience Manager (AEM) 

`Using Visual Studio Code with Intel® oneAPI Toolkits User Guide <https://www.intel.com/content/www/us/en/docs/oneapi/user-guide-vs-code/2024-0/overview.html>`_

:download:`PDF Version <pdf/oneapi_user-guide-vs-code.pdf>`

..
    
   **Project**

     Improve  usability and adoption for developers by creating Visual Studio Code (VS Code)
     extensions that enhance development with Intel oneAPI components.
   
   **Context**

     User feedback indicated that VS Code was the most popular interface for coding on the DPC++ and SYCL platforms.
     The development team created extensions for enhancing the user experience, and I worked on a a guide for how
     to install, configure, and use the extensions for a better user experience.

   **Achievements**

     - more than 85,000 downloads, with an average rating of 4.6 stars
     - improved user success for running samples in user studies by more than 25 percent 


  **Technical Details**
  
     Source files: reStructuredText
     Repository: internal GitHub repository
     Transformation: Sphinx to DITA (sphinx2dita)
     Web Platform: Adobe Experience Manager (AEM) 

