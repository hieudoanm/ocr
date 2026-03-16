import { NextPage } from 'next';
import dynamic from 'next/dynamic';

const OCR = dynamic(() => import('@ocr/components/OCR'), { ssr: false });

const ImagesOCRPage: NextPage = () => {
  return (
    <div className="min-h-screen">
      <OCR />
    </div>
  );
};

export default ImagesOCRPage;
