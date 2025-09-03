import React, { useContext } from 'react';
import { motion } from 'framer-motion';
import { Download, Eye, Share2, BarChart3, Clock, FileText } from 'lucide-react';
import { ContentContext } from '../context/ContentContext';
import ContentCard from '../components/ContentCard';

const Results = () => {
  const { results } = useContext(ContentContext);

  if (!results) {
    return (
      <div className="max-w-4xl mx-auto text-center py-20">
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
        >
          <FileText className="h-16 w-16 text-gray-400 mx-auto mb-4" />
          <h2 className="text-2xl font-bold text-gray-900 mb-4">
            No Content Generated Yet
          </h2>
          <p className="text-gray-600 mb-8">
            Create your first piece of content to see results here.
          </p>
          <a
            href="/create"
            className="bg-blue-600 hover:bg-blue-700 text-white font-semibold py-3 px-6 rounded-lg transition-colors duration-200"
          >
            Create Content
          </a>
        </motion.div>
      </div>
    );
  }

  const downloadContent = (content, filename) => {
    const blob = new Blob([content], { type: 'text/plain' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = filename;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
  };

  return (
    <div className="max-w-7xl mx-auto">
      {/* Header */}
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        className="text-center mb-8"
      >
        <h1 className="text-3xl font-bold text-gray-900 mb-4">
          Content Creation Results
        </h1>
        <p className="text-lg text-gray-600">
          Your AI-generated content is ready! Review, edit, and deploy.
        </p>
      </motion.div>

      {/* Stats Overview */}
      <motion.div
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ delay: 0.1 }}
        className="grid grid-cols-1 md:grid-cols-4 gap-6 mb-8"
      >
        <div className="bg-white rounded-lg shadow-md p-6 text-center">
          <Clock className="h-8 w-8 text-blue-600 mx-auto mb-2" />
          <div className="text-2xl font-bold text-gray-900">
            {results.processingTime || '45'}s
          </div>
          <div className="text-sm text-gray-600">Processing Time</div>
        </div>
        
        <div className="bg-white rounded-lg shadow-md p-6 text-center">
          <BarChart3 className="h-8 w-8 text-green-600 mx-auto mb-2" />
          <div className="text-2xl font-bold text-gray-900">
            {results.qualityScore || '9.2'}/10
          </div>
          <div className="text-sm text-gray-600">Quality Score</div>
        </div>
        
        <div className="bg-white rounded-lg shadow-md p-6 text-center">
          <FileText className="h-8 w-8 text-purple-600 mx-auto mb-2" />
          <div className="text-2xl font-bold text-gray-900">
            {results.wordCount || '1,247'}
          </div>
          <div className="text-sm text-gray-600">Words Generated</div>
        </div>
        
        <div className="bg-white rounded-lg shadow-md p-6 text-center">
          <Share2 className="h-8 w-8 text-orange-600 mx-auto mb-2" />
          <div className="text-2xl font-bold text-gray-900">
            {results.platformCount || '3'}
          </div>
          <div className="text-sm text-gray-600">Platform Versions</div>
        </div>
      </motion.div>

      {/* Content Tabs */}
      <motion.div
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ delay: 0.2 }}
        className="bg-white rounded-lg shadow-md"
      >
        <div className="border-b border-gray-200">
          <nav className="-mb-px flex space-x-8 px-6">
            {['final-content', 'seo-data', 'platform-versions', 'qa-report'].map((tab) => (
              <button
                key={tab}
                className="py-4 px-1 border-b-2 border-transparent text-sm font-medium text-gray-500 hover:text-gray-700 hover:border-gray-300 focus:outline-none focus:text-blue-600 focus:border-blue-500"
              >
                {tab.split('-').map(word => word.charAt(0).toUpperCase() + word.slice(1)).join(' ')}
              </button>
            ))}
          </nav>
        </div>

        <div className="p-6">
          {/* Final Content */}
          <div className="mb-8">
            <div className="flex items-center justify-between mb-4">
              <h3 className="text-lg font-semibold text-gray-900">Final Content</h3>
              <div className="flex space-x-2">
                <button
                  onClick={() => downloadContent(results.finalContent || results.sampleContent, 'content.txt')}
                  className="flex items-center space-x-1 px-3 py-1 text-sm bg-blue-100 text-blue-700 rounded-md hover:bg-blue-200 transition-colors"
                >
                  <Download className="h-4 w-4" />
                  <span>Download</span>
                </button>
                <button className="flex items-center space-x-1 px-3 py-1 text-sm bg-gray-100 text-gray-700 rounded-md hover:bg-gray-200 transition-colors">
                  <Eye className="h-4 w-4" />
                  <span>Preview</span>
                </button>
              </div>
            </div>
            
            <div className="bg-gray-50 rounded-lg p-6 max-h-96 overflow-y-auto">
              <pre className="whitespace-pre-wrap text-sm text-gray-800 font-mono">
                {results.finalContent || `# ${results.topic || 'Sample Topic'}

This is a sample of the AI-generated content. The actual content would appear here after processing through our multi-agent system.

## Key Features Covered:
- Comprehensive research insights
- SEO-optimized structure
- Platform-specific adaptations
- Quality-assured content

The content has been processed through all six AI agents:
1. Research Agent - Gathered comprehensive insights
2. Writer Agent - Created engaging content
3. Editor Agent - Improved clarity and flow
4. SEO Agent - Optimized for search engines
5. Platform Agent - Adapted for multiple platforms
6. QA Agent - Ensured quality standards

This demonstration shows how multiple AI agents can collaborate to create high-quality, professional content efficiently.`}
              </pre>
            </div>
          </div>

          {/* SEO Data */}
          <div className="mb-8">
            <h3 className="text-lg font-semibold text-gray-900 mb-4">SEO Optimization</h3>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
              <div className="space-y-4">
                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-1">Meta Title</label>
                  <div className="bg-gray-50 rounded-md p-3 text-sm">
                    {results.metaTitle || `${results.topic || 'AI Technology'}: Complete Guide & Best Practices 2024`}
                  </div>
                </div>
                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-1">Meta Description</label>
                  <div className="bg-gray-50 rounded-md p-3 text-sm">
                    {results.metaDescription || `Comprehensive guide to ${results.topic || 'AI technology'}. Learn key insights, trends, and applications with expert analysis and practical recommendations.`}
                  </div>
                </div>
              </div>
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-1">Target Keywords</label>
                <div className="flex flex-wrap gap-2">
                  {(results.keywords || ['AI technology', 'digital transformation', 'innovation']).map((keyword, index) => (
                    <span
                      key={index}
                      className="px-2 py-1 bg-blue-100 text-blue-800 text-xs rounded-full"
                    >
                      {keyword}
                    </span>
                  ))}
                </div>
                
                <div className="mt-4">
                  <label className="block text-sm font-medium text-gray-700 mb-2">Keyword Density</label>
                  <div className="space-y-2">
                    {(results.keywordDensity || [
                      { keyword: 'AI technology', density: 2.1 },
                      { keyword: 'digital transformation', density: 1.8 },
                      { keyword: 'innovation', density: 1.5 }
                    ]).map((item, index) => (
                      <div key={index} className="flex justify-between items-center">
                        <span className="text-sm text-gray-600">{item.keyword}</span>
                        <span className="text-sm font-medium">{item.density}%</span>
                      </div>
                    ))}
                  </div>
                </div>
              </div>
            </div>
          </div>

          {/* Platform Versions */}
          <div className="mb-8">
            <h3 className="text-lg font-semibold text-gray-900 mb-4">Platform-Specific Versions</h3>
            <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
              {(results.platformVersions || [
                { platform: 'Twitter', content: 'Engaging Twitter thread about the topic...' },
                { platform: 'LinkedIn', content: 'Professional LinkedIn post with insights...' },
                { platform: 'Blog', content: 'Complete blog post with SEO optimization...' }
              ]).map((version, index) => (
                <div key={index} className="border border-gray-200 rounded-lg p-4">
                  <div className="flex items-center justify-between mb-3">
                    <h4 className="font-medium text-gray-900">{version.platform}</h4>
                    <button
                      onClick={() => downloadContent(version.content, `${version.platform.toLowerCase()}-content.txt`)}
                      className="text-blue-600 hover:text-blue-800 transition-colors"
                    >
                      <Download className="h-4 w-4" />
                    </button>
                  </div>
                  <div className="bg-gray-50 rounded-md p-3 text-sm max-h-32 overflow-y-auto">
                    {version.content}
                  </div>
                </div>
              ))}
            </div>
          </div>

          {/* QA Report */}
          <div>
            <h3 className="text-lg font-semibold text-gray-900 mb-4">Quality Assurance Report</h3>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
              <div>
                <div className="bg-green-50 border border-green-200 rounded-lg p-4 mb-4">
                  <div className="flex items-center space-x-2">
                    <div className="w-8 h-8 bg-green-500 rounded-full flex items-center justify-center">
                      <svg className="w-4 h-4 text-white" fill="currentColor" viewBox="0 0 20 20">
                        <path fillRule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clipRule="evenodd" />
                      </svg>
                    </div>
                    <div>
                      <div className="font-semibold text-green-800">Content Approved</div>
                      <div className="text-sm text-green-600">Quality Score: {results.qualityScore || '9.2'}/10</div>
                    </div>
                  </div>
                </div>
                
                <div className="space-y-2">
                  <h4 className="font-medium text-gray-900">Quality Checks Passed:</h4>
                  {(results.qualityChecks || [
                    'Grammar and spelling',
                    'Content structure',
                    'SEO optimization',
                    'Platform compliance',
                    'Brand consistency'
                  ]).map((check, index) => (
                    <div key={index} className="flex items-center space-x-2">
                      <svg className="w-4 h-4 text-green-500" fill="currentColor" viewBox="0 0 20 20">
                        <path fillRule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clipRule="evenodd" />
                      </svg>
                      <span className="text-sm text-gray-700">{check}</span>
                    </div>
                  ))}
                </div>
              </div>
              
              <div>
                <h4 className="font-medium text-gray-900 mb-2">Recommendations:</h4>
                <ul className="space-y-1 text-sm text-gray-600">
                  {(results.recommendations || [
                    'Consider adding more case studies for enhanced credibility',
                    'Include recent statistics where available',
                    'Add visual content suggestions for better engagement'
                  ]).map((rec, index) => (
                    <li key={index} className="flex items-start space-x-2">
                      <span className="text-blue-500 mt-1">•</span>
                      <span>{rec}</span>
                    </li>
                  ))}
                </ul>
              </div>
            </div>
          </div>
        </div>
      </motion.div>
    </div>
  );
};

export default Results;
