import React from 'react';
import { motion } from 'framer-motion';
import { Clock, CheckCircle, AlertCircle } from 'lucide-react';

const ContentCard = ({ title, content, type, status, metrics }) => {
  const getStatusIcon = () => {
    switch (status) {
      case 'completed':
        return <CheckCircle className="h-5 w-5 text-green-500" />;
      case 'processing':
        return <Clock className="h-5 w-5 text-blue-500 animate-spin" />;
      case 'error':
        return <AlertCircle className="h-5 w-5 text-red-500" />;
      default:
        return null;
    }
  };

  const getTypeColor = () => {
    switch (type) {
      case 'blog':
        return 'bg-blue-100 text-blue-800';
      case 'social':
        return 'bg-green-100 text-green-800';
      case 'email':
        return 'bg-purple-100 text-purple-800';
      default:
        return 'bg-gray-100 text-gray-800';
    }
  };

  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      className="bg-white rounded-lg shadow-md border border-gray-200 p-6 hover:shadow-lg transition-shadow duration-200"
    >
      <div className="flex items-start justify-between mb-4">
        <div className="flex-1">
          <div className="flex items-center space-x-2 mb-2">
            <h3 className="text-lg font-semibold text-gray-900">{title}</h3>
            {getStatusIcon()}
          </div>
          <span className={`inline-block px-2 py-1 text-xs font-medium rounded-full ${getTypeColor()}`}>
            {type.charAt(0).toUpperCase() + type.slice(1)} Content
          </span>
        </div>
      </div>

      <div className="prose prose-sm max-w-none mb-4">
        <p className="text-gray-600 line-clamp-3">
          {content?.slice(0, 200)}
          {content?.length > 200 && '...'}
        </p>
      </div>

      {metrics && (
        <div className="grid grid-cols-3 gap-4 pt-4 border-t border-gray-100">
          <div className="text-center">
            <div className="text-sm font-medium text-gray-900">
              {metrics.wordCount || 0}
            </div>
            <div className="text-xs text-gray-500">Words</div>
          </div>
          <div className="text-center">
            <div className="text-sm font-medium text-gray-900">
              {metrics.readingTime || 0}
            </div>
            <div className="text-xs text-gray-500">Min Read</div>
          </div>
          <div className="text-center">
            <div className="text-sm font-medium text-gray-900">
              {metrics.seoScore || 0}/10
            </div>
            <div className="text-xs text-gray-500">SEO Score</div>
          </div>
        </div>
      )}
    </motion.div>
  );
};

export default ContentCard;
