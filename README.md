<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
<!-- [![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![GPL License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url] -->



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/jbirbal-skydom/TMX">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Detect Raven</h3>

  <p align="center">
    TMX is the serial control interface for the trackmaster treadmill protocol
    <br />
    <a href="https://github.com/jbirbal-skydom/TMX/"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/jbirbal-skydom/TMX/">View Demo</a>
    ·
    <a href="https://github.com/jbirbal-skydom/TMX/issues">Report Bug</a>
    ·
    <a href="https://github.com/jbirbal-skydom/TMX/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)

Using the trackmaster protocol, This simple tkinter GUI can control the speed and  elevation of the treadmil.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![Python][Python.org]][Python-url]
<!-- * [![OpenCV][opencv.org]][opencv-url]
* [![3433C][C-iso.com]][c-url]
* [![React][React.js]][React-url]
* [![Vue][Vue.js]][Vue-url]
* [![Angular][Angular.io]][Angular-url]
* [![Svelte][Svelte.dev]][Svelte-url]
* [![Laravel][Laravel.com]][Laravel-url]
* [![Bootstrap][Bootstrap.com]][Bootstrap-url]
* [![JQuery][JQuery.com]][JQuery-url] -->

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started
#

To run program use the executable
```
output\main.exe
```

# Modifications

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* Python 3.10 at [https://python.org](https://www.python.org/downloads/release/python-3100/)
  ```sh
  wget https://www.python.org/ftp/python/3.10.1/Python-3.10.1.tgz
  ```
    ```sh
  tar xzf Python-3.10.1.tgz
  ```
    ```sh
  cd Python-3.10.1 
  ./configure --enable-optimizations
  ```
  ```sh
  make altinstall
  ```



  

### Dependencies


1. We need to install a virtual environment and dependencies
2. Clone the repo
   ```sh
   git clone https://github.com/jbirbal-skydom/TMX/.git
   ```
3. Install virtual environment
   ```sh
   pip install virtualenv
   ```
4. To make virtual environment
   ```sh
   python -m venv .venv
   ```
5. Start VEnv
    ```sh
    .\.venv\Scripts\activate
    ```
6. Install dependencies
    ```sh
    python -m pip install -r requirements.txt
    ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Configure the settings JSON file
* Initialize our annotations file
    ```sh
    nano setting\config.jsonc
    ```
* edit the Config

  ```json
  {
	/****
	* DATASET PATHS
	****/
	"writePort": "COM1",
    "readPort": "COM2",
	"rate": 4800,
    "stopbits": 1,
    "Parity": "N",
    "bytes": 8,
    "timeout": 0,
    "Duplex": "full"
      ```


<!-- USAGE EXAMPLES -->
## Usage

Clicking the button up sends comand to increase the speed/elevation in relation to the set values respectfully. The increment are hard coded abut can be changed easily. 

The reference unit is the TMX 428: 
###### ---Any units that uses the treadmaster protocol should work.--- 
#
####
<div style="text-align: center;">

 ![tmx]

 </div>

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- 
<!-- 
- [ ] Image Capture ![product-roadmap-Icap]
  - [ ] Image Process![product-roadmap-Iproc]
  - [ ] Detect Image ![product-roadmap-DImg]

- [ ] Display![product-roadmap-Display]
- [ ] New Item ![product-roadmap-nItem] -->







See the [open issues](https://github.com/jbirbal-skydom/TMX/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Jason Birbal - skydom@zoho.com

Project Link: [https://github.com/jbirbal-skydom/TMX/](https://github.com/jbirbal-skydom/TMX/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* []()
* []()
* []()

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/jbirbal-skydom/TMX.svg?style=for-the-badge
[contributors-url]: https://github.com/jbirbal-skydom/TMX/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/jbirbal-skydom/TMX.svg?style=for-the-badge
[forks-url]: https://github.com/jbirbal-skydom/TMX/network/members
[stars-shield]: https://img.shields.io/github/stars/jbirbal-skydom/TMX.svg?style=for-the-badge
[stars-url]: https://github.com/jbirbal-skydom/TMX/stargazers
[issues-shield]: https://img.shields.io/github/issues/jbirbal-skydom/TMX.svg?style=for-the-badge
[issues-url]: https://github.com/jbirbal-skydom/TMX/issues
[license-shield]: https://img.shields.io/github/license/jbirbal-skydom/TMX?style=for-the-badge
[license-url]: https://github.com/jbirbal-skydom/TMX/blob/master/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username
[product-screenshot]: images/screenshot.jpg
[tmx]: images/tmx.jpg
[product-roadmap-DImg]: images/Drawing1/detectImage.png
[product-roadmap-Display]: images/Drawing1/Display.png
[product-roadmap-Icap]: images/Drawing1/ImageCapture.png
[product-roadmap-Iproc]: images/Drawing1/ImageProcessing.png
[product-roadmap-nItem]: images/Drawing1/NewItem.png
[product-roadmap-layout]: images/Drawing1/WarehouseLayout.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
[Python.org]: https://img.shields.io/badge/python-0769AD?style=for-the-badge&logo=python&logoColor=yellow
[Python-url]: https://python.org/
[opencv.org]: https://img.shields.io/badge/opencv-4A4A55?style=for-the-badge&logo=opencv
[opencv-url]: https://opencv.org/
[C-iso.com]: https://img.shields.io/badge/-Progam-4A4A55?style=for-the-badge&logo=C
[C-url]: https://www.iso.org/standard/74528.html
