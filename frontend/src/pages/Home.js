import React from 'react';
import { Link } from 'react-router-dom';
import { motion } from 'framer-motion';
import { ArrowRight, Bot, Zap, Target, Users, BarChart3, Shield } from 'lucide-react';

const Home = () => {
  const features = [
    {
      icon: Bot,
      title: 'Multi-Agent AI System',
      description: 'Six specialized AI agents working together to create perfect content'
    },
    {
      icon: Zap,
      title: 'Lightning Fast',
      description: 'Generate high-quality content in under 60 seconds'
    },
    {
      icon: Target,
      title: 'SEO Optimized',
      description: 'Automatically optimized for search engines and conversions'
    },
    {
      icon: Users,
      title: 'Platform Specific',
      description: 'Content adapted for Twitter, LinkedIn, blogs, and more'
    },
    {
      icon: BarChart3,
      title: 'Quality Assured',
      description: 'Built-in quality checks and approval workflows'
    },
    {
      icon: Shield,
      title: 'Reliable Results',
      description: 'Consistent, professional-grade content every time'
    }
  ];

  const agents = [
    { name: 'Research Agent', emoji: '🔍', task: 'Gathers insights' },
    { name: 'Writer Agent', emoji: '✍️', task: 'Creates content' },
    { name: 'Editor Agent', emoji: '📝', task: 'Improves quality' },
    { name: 'SEO Agent', emoji: '🎯', task: 'Optimizes visibility' },
    { name: 'Platform Agent', emoji: '📱', task: 'Adapts format' },
    { name: 'QA Agent', emoji: '✅', task: 'Ensures excellence' }
  ];

  return (
    <div className="max-w-7xl mx-auto">
      {/* Hero Section */}
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        className="text-center py-20"
      >
        <h1 className="text-5xl font-bold text-gray-900 mb-6">
          Smart Content Creation
          <span className="text-blue-600"> Pipeline</span>
        </h1>
        <p className="text-xl text-gray-600 mb-8 max-w-3xl mx-auto">
          Harness the power of AI multi-agent systems to create high-quality, 
          platform-optimized content in seconds. From research to publication-ready content.
        </p>
        <div className="flex justify-center space-x-4">
          <Link
            to="/create"
            className="bg-blue-600 hover:bg-blue-700 text-white font-semibold py-3 px-8 rounded-lg transition-colors duration-200 flex items-center space-x-2"
          >
            <span>Start Creating</span>
            <ArrowRight className="h-4 w-4" />
          </Link>
          <Link
            to="/about"
            className="bg-gray-200 hover:bg-gray-300 text-gray-800 font-semibold py-3 px-8 rounded-lg transition-colors duration-200"
          >
            Learn More
          </Link>
        </div>
      </motion.div>

      {/* Features Grid */}
      <motion.div
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ delay: 0.2 }}
        className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 mb-20"
      >
        {features.map((feature, index) => (
          <motion.div
            key={feature.title}
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.1 * index }}
            className="bg-white rounded-lg shadow-md p-6 hover:shadow-lg transition-shadow duration-200"
          >
            <feature.icon className="h-12 w-12 text-blue-600 mb-4" />
            <h3 className="text-lg font-semibold text-gray-900 mb-2">
              {feature.title}
            </h3>
            <p className="text-gray-600">
              {feature.description}
            </p>
          </motion.div>
        ))}
      </motion.div>

      {/* Agent Workflow */}
      <motion.div
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ delay: 0.4 }}
        className="bg-gradient-to-r from-blue-50 to-indigo-50 rounded-xl p-8 mb-20"
      >
        <h2 className="text-3xl font-bold text-center text-gray-900 mb-12">
          How Our AI Agents Work Together
        </h2>
        
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {agents.map((agent, index) => (
            <motion.div
              key={agent.name}
              initial={{ opacity: 0, scale: 0.9 }}
              animate={{ opacity: 1, scale: 1 }}
              transition={{ delay: 0.1 * index }}
              className="bg-white rounded-lg p-6 text-center shadow-sm hover:shadow-md transition-shadow duration-200"
            >
              <div className="text-4xl mb-3">{agent.emoji}</div>
              <h3 className="font-semibold text-gray-900 mb-2">{agent.name}</h3>
              <p className="text-sm text-gray-600">{agent.task}</p>
              
              {/* Connection Line */}
              {index < agents.length - 1 && (
                <div className="hidden lg:block absolute top-1/2 -right-3 w-6 h-0.5 bg-blue-300 transform -translate-y-1/2" />
              )}
            </motion.div>
          ))}
        </div>
        
        <div className="text-center mt-8">
          <p className="text-gray-600 mb-6">
            Each agent specializes in a specific task, ensuring optimal results through collaboration
          </p>
          <Link
            to="/create"
            className="inline-flex items-center space-x-2 bg-blue-600 hover:bg-blue-700 text-white font-semibold py-3 px-6 rounded-lg transition-colors duration-200"
          >
            <span>Try It Now</span>
            <ArrowRight className="h-4 w-4" />
          </Link>
        </div>
      </motion.div>

      {/* Stats Section */}
      <motion.div
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ delay: 0.6 }}
        className="bg-white rounded-lg shadow-md p-8 text-center"
      >
        <h2 className="text-2xl font-bold text-gray-900 mb-8">
          Trusted by Content Creators
        </h2>
        <div className="grid grid-cols-1 md:grid-cols-4 gap-8">
          <div>
            <div className="text-3xl font-bold text-blue-600 mb-2">98%</div>
            <div className="text-gray-600">Quality Score</div>
          </div>
          <div>
            <div className="text-3xl font-bold text-blue-600 mb-2">60s</div>
            <div className="text-gray-600">Average Time</div>
          </div>
          <div>
            <div className="text-3xl font-bold text-blue-600 mb-2">6</div>
            <div className="text-gray-600">AI Agents</div>
          </div>
          <div>
            <div className="text-3xl font-bold text-blue-600 mb-2">∞</div>
            <div className="text-gray-600">Possibilities</div>
          </div>
        </div>
      </motion.div>
    </div>
  );
};

export default Home;
