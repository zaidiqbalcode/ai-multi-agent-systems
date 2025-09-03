# Smart Content Pipeline - React Frontend Setup

## Quick Start

### 1. Install Node.js Dependencies
```bash
cd frontend
npm install
```

### 2. Start the Development Server
```bash
npm start
```

The React application will open in your browser at `http://localhost:3000`

## Available Scripts

In the frontend directory, you can run:

### `npm start`
Runs the app in development mode at [http://localhost:3000](http://localhost:3000).

### `npm run build`
Builds the app for production to the `build` folder.

### `npm test`
Launches the test runner in interactive watch mode.

## Backend API (Optional)

To connect with the Python backend:

### 1. Install Python Dependencies
```bash
pip install flask flask-cors
```

### 2. Start the API Server
```bash
python api.py
```

The API will run at `http://localhost:8000`

## Features

### 🎨 Modern React Interface
- Responsive design with Tailwind CSS
- Smooth animations with Framer Motion
- Interactive workflow visualization
- Real-time progress tracking

### 🤖 Multi-Agent Workflow
- Visual representation of agent collaboration
- Step-by-step progress indicator
- Real-time status updates
- Agent-specific animations

### 📊 Results Dashboard
- Comprehensive content analysis
- SEO optimization metrics
- Platform-specific versions
- Quality assurance reports

### 🔧 Configuration Options
- Multiple content types
- Various target audiences
- Different tone settings
- Platform selection
- API provider choice

## Project Structure

```
frontend/
├── public/
│   ├── index.html
│   └── manifest.json
├── src/
│   ├── components/
│   │   ├── Header.js
│   │   ├── AgentCard.js
│   │   ├── WorkflowVisualization.js
│   │   └── ContentCard.js
│   ├── pages/
│   │   ├── Home.js
│   │   ├── CreateContent.js
│   │   ├── Results.js
│   │   └── About.js
│   ├── context/
│   │   └── ContentContext.js
│   ├── App.js
│   ├── index.js
│   └── index.css
├── package.json
├── tailwind.config.js
└── postcss.config.js
```

## Environment Setup

### Development
The app runs in development mode with hot reloading enabled.

### Production
Build the app for production:
```bash
npm run build
```

### Deployment
The build folder can be deployed to any static hosting service like:
- Vercel
- Netlify
- GitHub Pages
- AWS S3

## Browser Support

The React app supports:
- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)

## Troubleshooting

### Common Issues

1. **Port 3000 in use**
   ```bash
   npm start -- --port 3001
   ```

2. **Module not found errors**
   ```bash
   rm -rf node_modules package-lock.json
   npm install
   ```

3. **Build issues**
   ```bash
   npm run build
   ```

### Performance

- The app uses lazy loading for optimal performance
- Images and assets are optimized
- Code splitting is implemented
- Service worker for caching (in production builds)

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request
