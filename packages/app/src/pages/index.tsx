import {
  LandingContent,
  LandingTemplate,
} from '@ocr/templates/LandingTemplate';
import { NextPage } from 'next';

const content: LandingContent = {
  navbar: {
    title: 'OCR Tool',
    buttonText: 'Open OCR',
    buttonHref: '/app',
  },
  hero: {
    title: 'Extract Text from Images Instantly',
    tagline:
      'Upload an image or screenshot and convert it into editable text directly in your browser.',
    buttonText: 'Start OCR',
    buttonHref: '/app',
  },
  features: {
    title: 'Features',
    items: [
      {
        id: 'fast-ocr',
        emoji: '⚡',
        title: 'Fast OCR Processing',
        description:
          'Quickly recognize and extract text from images using in-browser OCR.',
      },
      {
        id: 'privacy-first',
        emoji: '🔒',
        title: 'Privacy-First',
        description:
          'All processing happens locally in your browser. Your images never leave your device.',
      },
      {
        id: 'multiple-formats',
        emoji: '🖼️',
        title: 'Multiple Image Formats',
        description:
          'Supports PNG, JPG, WEBP, and screenshots for seamless text extraction.',
      },
      {
        id: 'copy-export',
        emoji: '📋',
        title: 'Copy or Export Text',
        description:
          'Instantly copy recognized text or export it for use in other tools.',
      },
      {
        id: 'multi-language',
        emoji: '🌍',
        title: 'Multi-Language Support',
        description: 'Recognize text in multiple languages with high accuracy.',
      },
      {
        id: 'simple-ui',
        emoji: '✨',
        title: 'Simple Interface',
        description:
          'Clean and distraction-free interface designed for quick workflows.',
      },
    ],
  },
  cta: {
    title: 'Convert Images to Text Now',
    description: 'A fast, private OCR tool that runs entirely in your browser.',
    buttonText: 'Open OCR Tool',
    buttonHref: '/app',
  },
  footer: {
    name: 'OCR Tool',
  },
};

const HomePage: NextPage = () => {
  return <LandingTemplate content={content} />;
};

export default HomePage;
