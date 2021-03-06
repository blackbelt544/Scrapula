// qpdfwriter.sip generated by MetaSIP on Fri Jul  4 10:09:32 2014
//
// This file is part of the QtGui Python extension module.
//
// Copyright (c) 2014 Riverbank Computing Limited <info@riverbankcomputing.com>
// 
// This file is part of PyQt5.
// 
// This file may be used under the terms of the GNU General Public License
// version 3.0 as published by the Free Software Foundation and appearing in
// the file LICENSE included in the packaging of this file.  Please review the
// following information to ensure the GNU General Public License version 3.0
// requirements will be met: http://www.gnu.org/copyleft/gpl.html.
// 
// If you do not wish to use this file under the terms of the GPL version 3.0
// then you may purchase a commercial license.  For more information contact
// info@riverbankcomputing.com.
// 
// This file is provided AS IS with NO WARRANTY OF ANY KIND, INCLUDING THE
// WARRANTY OF DESIGN, MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.


class QPdfWriter : QObject, QPagedPaintDevice
{
%TypeHeaderCode
#include <qpdfwriter.h>
%End

public:
    explicit QPdfWriter(const QString &filename);
    explicit QPdfWriter(QIODevice *device);
    virtual ~QPdfWriter();
    QString title() const;
    void setTitle(const QString &title);
    QString creator() const;
    void setCreator(const QString &creator);
    virtual bool newPage();
    virtual void setPageSize(QPagedPaintDevice::PageSize size);
    virtual void setPageSizeMM(const QSizeF &size);
    virtual void setMargins(const QPagedPaintDevice::Margins &m);

protected:
    virtual QPaintEngine *paintEngine() const;
    virtual int metric(QPaintDevice::PaintDeviceMetric id) const;

public:
%If (Qt_5_3_0 -)
    void setResolution(int resolution);
%End
%If (Qt_5_3_0 -)
    int resolution() const;
%End

private:
    QPdfWriter(const QPdfWriter &);
};
