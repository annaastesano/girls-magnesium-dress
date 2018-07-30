/**
 * @fileoverview Main js entry point.
 */
import { initPolyfills } from './polyfills';
import { initAnalytics } from './analytics';
import fullpage from 'fullpage.js/dist/jquery.fullpage'; // eslint-disable-line no-unused-vars
import jQuery from 'jquery';
import 'slick-carousel';

import ParallaxSection from './components/parallax-section';
import Header from './components/header';
import Registration from './components/registration';
import SliderSection from './components/slider-section';
import Accordion from './components/accordion';
import LearnMoreBtn from './components/learn-more-btn';

// Custom elements.
window.customElements.define('tr-header', Header);
window.customElements.define('tr-registration', Registration);
window.customElements.define('tr-slider-section', SliderSection);
window.customElements.define('tr-accordion', Accordion);
window.customElements.define('tr-parallax-section', ParallaxSection);
window.customElements.define('learn-more-btn', LearnMoreBtn);

initPolyfills();
initAnalytics();