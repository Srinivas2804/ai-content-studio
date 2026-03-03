import type { Metadata } from 'next'
import './globals.css'

export const metadata: Metadata = {
  title: 'ContentStudio — AI Repurposing Engine',
  description: 'Transform one piece of content into 12+ formats instantly with AI agents.',
}

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  )
}