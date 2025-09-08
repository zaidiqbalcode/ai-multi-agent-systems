import React, { useState, useContext } from 'react';
import { motion } from 'framer-motion';
import { useNavigate } from 'react-router-dom';
import toast from 'react-hot-toast';
import { Play, Settings, HelpCircle } from 'lucide-react';
import WorkflowVisualization from '../components/WorkflowVisualization';
import { ContentContext } from '../context/ContentContext';

const CreateContent = () => {
  const navigate = useNavigate();
  const { createContent } = useContext(ContentContext);
  const [isProcessing, setIsProcessing] = useState(false);
  const [currentStep, setCurrentStep] = useState(-1);
  
  const [formData, setFormData] = useState({
    topic: '',
    contentType: 'blog_post',
    targetAudience: 'professionals',
    tone: 'professional',
    platforms: ['blog'],
    keywords: '',
    apiProvider: 'backend', // Use pre-configured backend
    apiKey: '' // Not needed when using backend
  });

  const contentTypes = [
    { value: 'blog_post', label: 'Blog Post', description: 'Long-form content for websites' },
    { value: 'article', label: 'Article', description: 'News or magazine-style content' },
    { value: 'social_media', label: 'Social Media', description: 'Short-form social content' },
    { value: 'newsletter', label: 'Newsletter', description: 'Email newsletter content' },
    { value: 'whitepaper', label: 'Whitepaper', description: 'Technical documentation' }
  ];

  const audiences = [
    { value: 'general', label: 'General Audience' },
    { value: 'professionals', label: 'Business Professionals' },
    { value: 'students', label: 'Students & Learners' },
    { value: 'entrepreneurs', label: 'Entrepreneurs' },
    { value: 'technical', label: 'Technical Experts' }
  ];

  const tones = [
    { value: 'professional', label: 'Professional' },
    { value: 'casual', label: 'Casual & Friendly' },
    { value: 'formal', label: 'Formal' },
    { value: 'conversational', label: 'Conversational' },
    { value: 'authoritative', label: 'Authoritative' }
  ];

  const platforms = [
    { value: 'blog', label: 'Blog/Website', icon: '📝' },
    { value: 'twitter', label: 'Twitter', icon: '🐦' },
    { value: 'linkedin', label: 'LinkedIn', icon: '💼' },
    { value: 'facebook', label: 'Facebook', icon: '📘' },
    { value: 'instagram', label: 'Instagram', icon: '📸' }
  ];

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: value
    }));
  };

  const handlePlatformChange = (platform) => {
    setFormData(prev => ({
      ...prev,
      platforms: prev.platforms.includes(platform)
        ? prev.platforms.filter(p => p !== platform)
        : [...prev.platforms, platform]
    }));
  };

  const simulateWorkflow = async () => {
    const steps = ['Research', 'Writing', 'Editing', 'SEO', 'Platform', 'QA'];
    
    for (let i = 0; i < steps.length; i++) {
      setCurrentStep(i);
      await new Promise(resolve => setTimeout(resolve, 1000 + Math.random() * 1000));
    }
    
    setCurrentStep(steps.length);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    if (!formData.topic.trim()) {
      toast.error('Please enter a content topic');
      return;
    }

    if (formData.platforms.length === 0) {
      toast.error('Please select at least one platform');
      return;
    }

    setIsProcessing(true);
    
    try {
      // Show workflow visualization
      await simulateWorkflow();
      
      // Prepare data for content creation
      const contentData = {
        ...formData,
        keywords: formData.keywords ? formData.keywords.split(',').map(k => k.trim()) : []
      };
      
  // Create content (this would call the actual API in production)
  await createContent(contentData); // result not needed directly here
      
      toast.success('Content created successfully!');
      navigate('/results');
      
    } catch (error) {
      toast.error('Failed to create content: ' + error.message);
    } finally {
      setIsProcessing(false);
      setCurrentStep(-1);
    }
  };

  return (
    <div className="max-w-7xl mx-auto">
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        className="text-center mb-8"
      >
        <h1 className="text-3xl font-bold text-gray-900 mb-4">
          Create Content with AI Agents
        </h1>
        <p className="text-lg text-gray-600 max-w-2xl mx-auto">
          Configure your content requirements and let our AI agents collaborate to create 
          high-quality, optimized content for your needs.
        </p>
      </motion.div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
        {/* Content Form */}
        <motion.div
          initial={{ opacity: 0, x: -20 }}
          animate={{ opacity: 1, x: 0 }}
          className="lg:col-span-2"
        >
          <div className="bg-white rounded-lg shadow-md p-6">
            <form onSubmit={handleSubmit} className="space-y-6">
              {/* Topic Input */}
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-2">
                  Content Topic *
                </label>
                <input
                  type="text"
                  name="topic"
                  value={formData.topic}
                  onChange={handleInputChange}
                  placeholder="e.g., Artificial Intelligence in Healthcare"
                  className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                  disabled={isProcessing}
                />
              </div>

              {/* Content Type */}
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-2">
                  Content Type
                </label>
                <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
                  {contentTypes.map((type) => (
                    <label
                      key={type.value}
                      className={`relative flex items-center p-3 border rounded-lg cursor-pointer hover:bg-gray-50 ${
                        formData.contentType === type.value
                          ? 'border-blue-500 bg-blue-50'
                          : 'border-gray-300'
                      }`}
                    >
                      <input
                        type="radio"
                        name="contentType"
                        value={type.value}
                        checked={formData.contentType === type.value}
                        onChange={handleInputChange}
                        className="sr-only"
                        disabled={isProcessing}
                      />
                      <div>
                        <div className="font-medium text-sm">{type.label}</div>
                        <div className="text-xs text-gray-500">{type.description}</div>
                      </div>
                    </label>
                  ))}
                </div>
              </div>

              {/* Target Audience */}
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-2">
                  Target Audience
                </label>
                <select
                  name="targetAudience"
                  value={formData.targetAudience}
                  onChange={handleInputChange}
                  className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                  disabled={isProcessing}
                >
                  {audiences.map((audience) => (
                    <option key={audience.value} value={audience.value}>
                      {audience.label}
                    </option>
                  ))}
                </select>
              </div>

              {/* Tone */}
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-2">
                  Content Tone
                </label>
                <select
                  name="tone"
                  value={formData.tone}
                  onChange={handleInputChange}
                  className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                  disabled={isProcessing}
                >
                  {tones.map((tone) => (
                    <option key={tone.value} value={tone.value}>
                      {tone.label}
                    </option>
                  ))}
                </select>
              </div>

              {/* Target Platforms */}
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-2">
                  Target Platforms
                </label>
                <div className="grid grid-cols-2 md:grid-cols-3 gap-3">
                  {platforms.map((platform) => (
                    <label
                      key={platform.value}
                      className={`relative flex items-center p-3 border rounded-lg cursor-pointer hover:bg-gray-50 ${
                        formData.platforms.includes(platform.value)
                          ? 'border-blue-500 bg-blue-50'
                          : 'border-gray-300'
                      }`}
                    >
                      <input
                        type="checkbox"
                        checked={formData.platforms.includes(platform.value)}
                        onChange={() => handlePlatformChange(platform.value)}
                        className="sr-only"
                        disabled={isProcessing}
                      />
                      <div className="flex items-center space-x-2">
                        <span className="text-lg">{platform.icon}</span>
                        <span className="text-sm font-medium">{platform.label}</span>
                      </div>
                    </label>
                  ))}
                </div>
              </div>

              {/* Keywords */}
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-2">
                  Target Keywords (Optional)
                </label>
                <input
                  type="text"
                  name="keywords"
                  value={formData.keywords}
                  onChange={handleInputChange}
                  placeholder="Enter keywords separated by commas"
                  className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                  disabled={isProcessing}
                />
                <p className="text-xs text-gray-500 mt-1">
                  e.g., AI healthcare, medical technology, digital transformation
                </p>
              </div>

              {/* API Configuration */}
              <div className="border-t pt-6">
                <h3 className="text-lg font-medium text-gray-900 mb-4 flex items-center">
                  <Settings className="h-5 w-5 mr-2" />
                  API Configuration
                </h3>
                
                <div className="space-y-4">
                  <div>
                    <label className="block text-sm font-medium text-gray-700 mb-2">
                      API Provider
                    </label>
                    <select
                      name="apiProvider"
                      value={formData.apiProvider}
                      onChange={handleInputChange}
                      className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                      disabled={isProcessing}
                    >
                      <option value="backend">Backend API (Pre-configured with your keys)</option>
                      <option value="openai">OpenAI GPT (Manual Key Entry)</option>
                      <option value="google">Google Gemini (Manual Key Entry)</option>
                    </select>
                  </div>

                  {formData.apiProvider === 'backend' && (
                    <div className="bg-green-50 border border-green-200 rounded-md p-3">
                      <div className="flex items-start space-x-2">
                        <div className="w-4 h-4 bg-green-500 rounded-full mt-0.5 flex-shrink-0"></div>
                        <div>
                          <p className="text-sm font-medium text-green-800">
                            Using Pre-configured Backend
                          </p>
                          <p className="text-xs text-green-600 mt-1">
                            Your Google Gemini API key is already configured in the backend. 
                            No additional setup required!
                          </p>
                        </div>
                      </div>
                    </div>
                  )}

                  {formData.apiProvider !== 'backend' && (
                    <div>
                      <label className="block text-sm font-medium text-gray-700 mb-2">
                        API Key
                      </label>
                      <input
                        type="password"
                        name="apiKey"
                        value={formData.apiKey}
                        onChange={handleInputChange}
                        placeholder="Enter your API key"
                        className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                        disabled={isProcessing}
                      />
                      <div className="flex items-start space-x-2 mt-2">
                        <HelpCircle className="h-4 w-4 text-blue-500 mt-0.5 flex-shrink-0" />
                        <p className="text-xs text-gray-500">
                          {formData.apiProvider === 'openai' 
                            ? 'Get your API key from OpenAI Platform'
                            : 'Get your API key from Google AI Studio'
                          }
                        </p>
                      </div>
                    </div>
                  )}
                </div>
              </div>

              {/* Submit Button */}
              <button
                type="submit"
                disabled={isProcessing}
                className={`w-full flex items-center justify-center space-x-2 py-3 px-6 rounded-lg font-semibold transition-colors duration-200 ${
                  isProcessing
                    ? 'bg-gray-400 cursor-not-allowed'
                    : 'bg-blue-600 hover:bg-blue-700 text-white'
                }`}
              >
                {isProcessing ? (
                  <>
                    <div className="w-5 h-5 border-2 border-white border-t-transparent rounded-full animate-spin" />
                    <span>Creating Content...</span>
                  </>
                ) : (
                  <>
                    <Play className="h-5 w-5" />
                    <span>Generate Content</span>
                  </>
                )}
              </button>
            </form>
          </div>
        </motion.div>

        {/* Workflow Visualization */}
        <motion.div
          initial={{ opacity: 0, x: 20 }}
          animate={{ opacity: 1, x: 0 }}
          className="lg:col-span-1"
        >
          <WorkflowVisualization currentStep={currentStep} />
        </motion.div>
      </div>
    </div>
  );
};

export default CreateContent;
